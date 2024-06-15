import reflex as rx
from personal_web.styles.styles import *

def navbar_menu_item_link(text: str, id_scroll: str):
    return  rx.menu.item(
        text,
        style = button_secondary_hover,
        on_click = rx.scroll_to(id_scroll),
    )