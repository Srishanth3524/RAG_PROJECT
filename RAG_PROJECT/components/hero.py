import reflex as rx

def hero():
    return rx.vstack(
        rx.box(
            rx.text("Next Generation OS", font_size="16px", font_weight="800", background_image="linear-gradient(90deg, #c084fc, #f472b6)", background_clip="text", color="transparent", text_transform="uppercase", margin_bottom="10px", text_align="center", letter_spacing="3px", style={"filter": "drop-shadow(0 0 8px rgba(244, 114, 182, 0.5))"}),
            rx.heading(
                rx.text.span("Unlock The Power Of\n", color="#f8fafc"),
                rx.text.span("AI Document Intelligence", background_image="linear-gradient(135deg, #a855f7, #ec4899, #ef4444)", background_clip="text", color="transparent", style={"filter": "drop-shadow(0 0 15px rgba(236, 72, 153, 0.3))"}),
                size="9",
                weight="bold",
                text_align="center",
                line_height="1.1",
                style={"font_size": "clamp(3.5rem, 6vw, 5rem)", "letter_spacing": "-2px"}
            ),
            rx.text(
                "Instantly chat with your internal documents using advanced open-source RAG models. Secure, private, and breathtakingly fast.",
                color="#94a3b8",
                font_size="22px",
                text_align="center",
                max_width="700px",
                margin_y="30px",
                margin_x="auto",
                line_height="1.6"
            ),
            rx.hstack(
                rx.button(
                    "Get Started Now",
                    rx.icon(tag="rocket", size=20, margin_left="8px"),
                    on_click=rx.redirect("/upload"),
                    background="linear-gradient(135deg, #8b5cf6, #d946ef)",
                    color="white",
                    size="4",
                    radius="full",
                    padding_x="40px",
                    padding_y="28px",
                    font_size="18px",
                    font_weight="700",
                    border="1px solid rgba(255, 255, 255, 0.2)",
                    box_shadow="0 0 30px rgba(217, 70, 239, 0.5), inset 0 2px 5px rgba(255,255,255,0.3)",
                    style={"_hover": {"transform": "translateY(-3px)", "box_shadow": "0 0 40px rgba(217, 70, 239, 0.7), inset 0 2px 5px rgba(255,255,255,0.4)"}, "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)"}
                ),
                rx.button(
                    "View History",
                    on_click=rx.redirect("/history"),
                    variant="outline",
                    size="4",
                    radius="full",
                    color_scheme="gray",
                    padding_x="40px",
                    padding_y="28px",
                    font_size="18px",
                    font_weight="700",
                    border="2px solid rgba(148, 163, 184, 0.2)",
                    color="#f1f5f9",
                    style={"_hover": {"background": "rgba(255,255,255,0.05)", "border_color": "rgba(148, 163, 184, 0.4)", "box_shadow": "0 0 20px rgba(255,255,255,0.05)"}, "transition": "all 0.3s ease"}
                ),
                spacing="6",
                justify="center",
                margin_top="10px"
            ),
            width="100%",
            margin_top="16vh",
            z_index="10",
            position="relative"
        ),
        # Glow Effect Orb Background
        rx.box(
            position="absolute",
            top="15%",
            left="50%",
            transform="translateX(-50%)",
            width="60vw",
            height="50vh",
            background="radial-gradient(ellipse, rgba(139, 92, 246, 0.15) 0%, rgba(2, 6, 23, 0) 70%)",
            z_index="0",
            pointer_events="none",
            style={"filter": "blur(60px)"}
        ),
        # Statistics/Feature Cards Row
        rx.hstack(
            feature_card("Sub-second Speed", "Lightning-fast semantic search", "zap"),
            feature_card("Zero Data Leaks", "Session-based local vector store", "shield-check"),
            feature_card("Open Models", "Powered by Llama 3 on Groq", "cpu"),
            spacing="8",
            margin_top="80px",
            justify="center",
            width="100%",
            wrap="wrap",
            z_index="10"
        ),
        width="100%",
        padding="20px",
        min_height="100vh",
        background="radial-gradient(circle at top center, #0f172a 0%, #020617 100%)",
        align="center",
        position="relative",
        overflow="hidden"
    )

def feature_card(title: str, description: str, icon_tag: str):
    return rx.vstack(
        rx.box(
            rx.icon(tag=icon_tag, size=28, color="#a78bfa"),
            padding="14px",
            background="rgba(139, 92, 246, 0.1)",
            border_radius="14px",
            margin_bottom="16px",
            style={"box_shadow": "inset 0 0 20px rgba(139, 92, 246, 0.2), 0 0 15px rgba(139, 92, 246, 0.1)"}
        ),
        rx.text(title, font_weight="800", font_size="20px", color="#f8fafc"),
        rx.text(description, color="#94a3b8", font_size="15px", text_align="center", line_height="1.5"),
        align="center",
        padding="32px",
        background="rgba(15, 23, 42, 0.4)",
        backdrop_filter="blur(16px)",
        border_radius="24px",
        border="1px solid rgba(255, 255, 255, 0.05)",
        box_shadow="0 10px 30px -5px rgba(0, 0, 0, 0.5)",
        width="300px",
        style={"_hover": {"transform": "translateY(-8px) scale(1.02)", "box_shadow": "0 20px 40px -5px rgba(139, 92, 246, 0.15)", "background": "rgba(30, 41, 59, 0.5)", "border": "1px solid rgba(255, 255, 255, 0.1)"}, "transition": "all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275)"}
    )