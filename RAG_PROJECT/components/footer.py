import reflex as rx

def footer():
    return rx.grid(
        rx.text("© 2026 RAG PROJECT. Secured & Private.", text_align="center", color="#64748b", font_size="14px", letter_spacing="1px"),
        padding="20px",
        bg="rgba(2, 6, 23, 0.9)",
        border_top="1px solid rgba(255, 255, 255, 0.05)",
        position="fixed",
        bottom="0",
        width="100%",
        z_index="50"
    )