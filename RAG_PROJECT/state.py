import reflex as rx
import requests

BASE_URL = "http://localhost:8000"

def query_backend(question: str):
    try:
        response = requests.post(
            f"{BASE_URL}/query",
            json={"question": question}
        )
        return response.json().get("answer", "No response")
    except Exception as e:
        return f"Error: {str(e)}"


class State(rx.State):
    question: str = ""
    answer: str = ""
    loading: bool = False

    def get_answer(self):
        self.loading = True
        self.answer = ""
        yield

        result = query_backend(self.question)

        self.answer = result
        self.loading = False