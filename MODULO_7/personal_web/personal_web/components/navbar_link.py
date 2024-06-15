import reflex as rx
from personal_web.styles.styles import *

def navbar_link(text: str, id_scroll: str):
    return rx.link(
        rx.text(
            text,
            style = text_could_hover
        ),
        text_decoration = "none",
        color = Color.TEXT.value,
        on_click = rx.scroll_to(id_scroll)
    )