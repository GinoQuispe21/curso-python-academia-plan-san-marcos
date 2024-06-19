import reflex as rx
from personal_web.styles.styles import *
from personal_web.constants import constants_user as const
from personal_web.components.navbar_link import navbar_link
from personal_web.components.navbar_menu_item_link import navbar_menu_item_link

def navbar():
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.heading(
                    const.USERNAME,
                    style = heading_navbar,
                    as_ = "h3"
                ),
                rx.hstack(
                    navbar_link("Experencia", "/#"),
                    navbar_link("Educacion", "/#"),
                    navbar_link("Proyectos", "/#"),
                    navbar_link("Sobre mi", "/#"),
                    justify = "end",
                    spacing = "5"
                ),
                align_items = "center",
                justify = "between",
                padding_x = "3em",
                padding_y = "1em"
            )
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.heading(
                    const.USERNAME,
                    style = heading_navbar,
                    as_ = "h3"
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size = 30)
                    ),
                    rx.menu.content(
                        navbar_menu_item_link("Experiencia", "/#"),
                        navbar_menu_item_link("Educacion", "/#"),
                        navbar_menu_item_link("Proyectos", "/#"),
                        navbar_menu_item_link("Sobre mi", "/#"),
                    ),
                    justify = "end"
                ),
                align_items = "center",
                justify = "between",
            ),
            padding_y = "2em",
            padding_x = "3em",
        ),
        border_bottom = border_spacer,
        position = "sticky",
        top = "0px",
        z_index = "999",
        width = "100%",
        background_color = Color.BACKGROUND
    )