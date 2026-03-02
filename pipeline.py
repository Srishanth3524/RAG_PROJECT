# ================================
# Corrective RAG - Single Script
# ================================

# Step 1: Imports
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()


# =========================================
# Step 2: Sample Documents (Replace later)
# =========================================

documents = [
    Document(
        page_content="LangChain helps developers build LLM applications easily.",
        metadata={"source": "doc1"}
    ),
    Document(
        page_content="Chroma is a vector database optimized for LLM-based search.",
        metadata={"source": "doc2"}
    ),
    Document(
        page_content="Embeddings convert text into high-dimensional vectors.",
        metadata={"source": "doc3"}
    ),
    Document(
        page_content="OpenAI provides powerful embedding models.",
        metadata={"source": "doc4"}
    ),
]


# =========================================
# Step 3: Initialize Embedding Model
# =========================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================================
# Step 4: Create Vector Store
# =========================================

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)


# =========================================
# Step 5: Convert to Retriever
# =========================================

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 2,
        "lambda_mult": 0.7
    }
)


# =========================================
# Step 6: Initialize LLM (Groq)
# =========================================

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)



# =========================================
# Utility: Format Retrieved Docs
# =========================================

def format_docs(docs):
    context = "\n\n".join([doc.page_content for doc in docs])
    sources = [doc.metadata.get("source", "unknown") for doc in docs]
    return context, sources


# =========================================
# Step 7: Corrective RAG Function
# =========================================

def corrective_rag(query):

    print("\n🔎 Initial Retrieval...")

    # Initial retrieval
    retrieved_docs = retriever.invoke(query)
    context, sources = format_docs(retrieved_docs)

    # -----------------------------
    # Step 7A: Retrieval Evaluation
    # -----------------------------
    evaluation_prompt = f"""
    Query: {query}

    Retrieved Context:
    {context}

    Are these documents relevant enough to answer the query?
    Respond strictly with YES or NO.
    """

    evaluation = llm.invoke(evaluation_prompt).content.strip()
    print("Relevance Check:", evaluation)

    # ---------------------------------
    # Step 7B: If NOT relevant -> Rewrite
    # ---------------------------------
    if "NO" in evaluation.upper():

        print("✍️ Rewriting Query...")

        rewrite_prompt = f"""
        The query "{query}" did not retrieve relevant documents.
        Rewrite it to improve retrieval quality.
        Only return the improved query.
        """

        improved_query = llm.invoke(rewrite_prompt).content.strip()
        print("Improved Query:", improved_query)

        # Re-retrieve with improved query
        retrieved_docs = retriever.invoke(improved_query)
        context, sources = format_docs(retrieved_docs)

    # ---------------------------------
    # Step 7C: Final Answer Generation
    # ---------------------------------
    final_prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question: {query}

    Also mention the sources used at the end.
    """

    answer = llm.invoke(final_prompt).content

    return answer, sources


# =========================================
# Step 8: Run Query
# =========================================

if __name__ == "__main__":

    query = "What is LangChain?"

    final_answer, sources = corrective_rag(query)

    print("\n📌 Final Answer:\n")
    print(final_answer)

    print("\n📚 Sources:", sources)