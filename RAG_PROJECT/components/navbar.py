import reflex as rx

def navbar():
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.icon(tag="layers", size=28, color="#8b5cf6", style={"filter": "drop-shadow(0 0 8px rgba(139, 92, 246, 0.8))"}),
                rx.text("DocuSearch AI", font_size="24px", font_weight="900", background_image="linear-gradient(90deg, #a78bfa, #c084fc, #e879f9)", background_clip="text", color="transparent", letter_spacing="-0.5px"),
                align="center",
                spacing="3",
                style={"cursor": "pointer", "_hover": {"transform": "scale(1.02)"}, "transition": "transform 0.3s ease"}
            ),
            rx.spacer(),
            rx.hstack(
                rx.link("Home", href="/", style={"_hover": {"color": "#c084fc", "text_shadow": "0 0 8px rgba(192, 132, 252, 0.5)"}, "transition": "all 0.3s"}, font_weight="600", color="#94a3b8"),
                rx.link("Upload", href="/upload", style={"_hover": {"color": "#c084fc", "text_shadow": "0 0 8px rgba(192, 132, 252, 0.5)"}, "transition": "all 0.3s"}, font_weight="600", color="#94a3b8"),
                rx.link("Chat", href="/chat", style={"_hover": {"color": "#c084fc", "text_shadow": "0 0 8px rgba(192, 132, 252, 0.5)"}, "transition": "all 0.3s"}, font_weight="600", color="#94a3b8"),
                rx.link("History", href="/history", style={"_hover": {"color": "#c084fc", "text_shadow": "0 0 8px rgba(192, 132, 252, 0.5)"}, "transition": "all 0.3s"}, font_weight="600", color="#94a3b8"),
                spacing="7",
            ),
            width="100%",
            padding_x="40px",
            padding_y="20px",
            max_width="1200px",
            margin="0 auto"
        ),
        width="100%",
        position="fixed",
        top="0",
        z_index="100",
        background="rgba(2, 6, 23, 0.65)",
        backdrop_filter="blur(16px)",
        border_bottom="1px solid rgba(255, 255, 255, 0.05)",
        box_shadow="0 4px 30px rgba(0, 0, 0, 0.5)"
    )
