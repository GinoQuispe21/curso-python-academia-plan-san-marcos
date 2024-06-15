import reflex as rx
from personal_web.styles.styles import *

def main_button(icon_str: str, text: str, url_str: str, size_str: str):
    return rx.link(
        rx.button(
            rx.icon(
                icon_str
            ),
            text,
            size = size_str,
            style = main_button_style
        ),
        href = url_str,
        is_external = True
    )

def secondary_button(icon_str: str, text: str, url_str: str, size_str: str):
    return rx.link(
        rx.button(
            rx.icon(
                icon_str
            ),
            text,
            size = size_str,
            style = secondary_button_style
        ),
        href = url_str,
    )