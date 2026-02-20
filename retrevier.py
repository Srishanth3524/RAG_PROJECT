from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

# -----------------------------
# 1️⃣ Create Documents
# -----------------------------
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# -----------------------------
# 2️⃣ Initialize Embedding Model
# -----------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# 3️⃣ Create Vector Store
# -----------------------------
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

# -----------------------------
# 4️⃣ Create Retriever
# -----------------------------
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 2, "lambda_mult": 1}
)

# -----------------------------
# 5️⃣ Query
# -----------------------------
query = "What is LangChain?"

retrieved_docs = retriever.invoke(query)

# Combine retrieved text properly
context = "\n".join([doc.page_content for doc in retrieved_docs])

# -----------------------------
# 6️⃣ Initialize Groq LLM
# -----------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# -----------------------------
# 7️⃣ RAG Prompt
# -----------------------------
prompt = f"""
You are an AI assistant.
Answer the question based only on the context below.

Context:
{context}

Question:
{query}

Answer:
"""

# -----------------------------
# 8️⃣ Get Answer
# -----------------------------
answer = llm.invoke(prompt)

print("Retrieved Context:\n", context)
print("\nFinal Answer:\n", answer.content)
