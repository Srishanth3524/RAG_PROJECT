from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

topic = input("Enter your topic: ")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain the topic in simple words: {topic}"
)

chain = prompt | llm
result = chain.invoke({"topic": topic})

# Print result
print("\nResponse:\n")
print(result.content)