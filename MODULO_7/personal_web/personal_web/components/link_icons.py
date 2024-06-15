import reflex as rx

def link_icons(icon_str: str, url: str, size: int):
    return rx.link(
        rx.icon(
            icon_str,
            size = size,
            color = "black"
        ),
        href = url,
        is_external = True
    )