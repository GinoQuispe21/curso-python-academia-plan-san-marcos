import reflex as rx
from personal_web.styles.styles import *

def section_header_icon(icon_str: str, text_heading: str):
    return rx.hstack(
        rx.icon(
            icon_str,
            size = 40
        ),
        rx.text(
            text_heading,
            font_size = TextSizes.SECTION_HEADING.value,
            line_height = "1.2em",
            weight = "bold"
        ),
        spacing = "6"
    )