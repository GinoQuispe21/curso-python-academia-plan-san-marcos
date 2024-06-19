import reflex as rx

def link_icons(icon_str: str, url: str, size: int):
    return rx.link(
        rx.icon(
            icon_str,
            size = size,
            color = rx.color_mode_cond(light = "black", dark = "white")
        ),
        href = url,
        is_external = True
    )