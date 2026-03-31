import reflex as rx
from RAG_PROJECT.components.navbar import navbar
from RAG_PROJECT.components.hero import hero
from RAG_PROJECT.components.footer import footer

def home():
    return rx.vstack(
        navbar(),
        hero(),
        footer(),
    )

