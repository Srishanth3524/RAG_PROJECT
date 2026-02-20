import os
import shutil
from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

if os.path.exists("chroma_db"):
    shutil.rmtree("chroma_db")


text_loader = TextLoader("cricket.txt")
text_docs = text_loader.load()

pdf_loader = PyPDFLoader("dances.pdf")
pdf_docs = pdf_loader.load()

pdf_docs = pdf_loader.load()
text_docs = text_loader.load()

all_docs = pdf_docs + text_docs



cleaned_docs = []
for doc in all_docs:
    doc.metadata = {
        "source": doc.metadata.get("source"),
        "page": doc.metadata.get("page", 0)
    }
    cleaned_docs.append(doc)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=200
)

split_docs = text_splitter.split_documents(cleaned_docs)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma.from_documents(
    documents=split_docs,
    embedding=embedding_model,
    persist_directory="./chroma_db",
    collection_name="fresh_session"
)

print("✅ Vector database built successfully!")
