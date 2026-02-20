from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Initialize Groq model
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

st.header("Research Tool (Static Prompt)")

user_input = st.text_input("Enter your topic")

if st.button("Summarize"):

    if user_input.strip() == "":
        st.warning("Please enter a topic.")
    else:
        # 🔹 Static Prompt
        static_prompt = f"""
        You are an AI research assistant.
        Explain the following topic in a clear and beginner-friendly way:

        Topic: {user_input}

        Provide:
        - Simple explanation
        - Key points
        - Real-world example
        """

        result = model.invoke(static_prompt)

        st.write(result.content)
