import reflex as rx
import requests

# =========================
# Backend Connection
# =========================
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


# =========================
# State
# =========================
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


# =========================
# COMPONENTS
# =========================

# 🔹 Navbar
def navbar():
    return rx.hstack(
        rx.heading("⚡ RAG AI", size="4", color="cyan"),
        rx.spacer(),
        rx.hstack(
            rx.link("Home"),
            rx.link("Chat"),
            rx.link("About"),
            spacing="6",
            color="gray.300"
        ),
        padding="20px",
        bg="rgba(0,0,0,0.7)",
        backdrop_filter="blur(10px)",
        border_bottom="1px solid rgba(255,255,255,0.1)",
        width="100%"
    )


# 🔹 Hero Section
def hero():
    return rx.vstack(
        rx.heading(
            "Ask Anything 🚀",
            size="8",
            bg_gradient="linear(to-r, cyan, blue)",
            bg_clip="text"
        ),
        rx.text(
            "Your intelligent RAG assistant powered by backend AI",
            color="gray.400",
            font_size="18px"
        ),
        align="center",
        spacing="4",
        padding_top="60px"
    )


# 🔹 Chat Section
def chat_section():
    return rx.vstack(

        # Input Box
        rx.input(
            placeholder="Type your question...",
            value=State.question,
            on_change=State.set_question,
            width="100%",
            size="3",
            border_radius="12px",
            padding="20px",
            bg="rgba(255,255,255,0.05)",
            border="1px solid rgba(255,255,255,0.1)",
            color="white"
        ),

        # Button
        rx.button(
            "Ask AI",
            on_click=State.get_answer,
            is_loading=State.loading,
            size="3",
            border_radius="12px",
            bg_gradient="linear(to-r, cyan, blue)",
            color="white",
            width="100%"
        ),

        # Response Box
        rx.box(
            rx.text(
                State.answer,
                color="white"
            ),
            margin_top="20px",
            padding="20px",
            border_radius="15px",
            bg="rgba(255,255,255,0.05)",
            border="1px solid rgba(255,255,255,0.1)",
            width="100%",
            min_height="100px"
        ),

        spacing="5",
        width="50%",
        margin_top="40px"
    )


# 🔹 Footer
def footer():
    return rx.hstack(
        rx.text(
            "© 2026 RAG Project • Built with ❤️ using Reflex",
            color="gray.500"
        ),
        justify="center",
        padding="25px",
        border_top="1px solid rgba(255,255,255,0.1)",
        width="100%",
        margin_top="60px"
    )


# =========================
# Main Page
# =========================
def index():
    return rx.box(
        rx.vstack(
            navbar(),
            hero(),
            chat_section(),
            footer(),
            align="center",
        ),

        # 🌌 Background Gradient
        min_height="100vh",
        bg="linear-gradient(135deg, #0f172a, #020617)",
        color="white"
    )


# =========================
# App Init
# =========================
app = rx.App()
app.add_page(index)