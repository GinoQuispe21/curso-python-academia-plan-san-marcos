import reflex as rx
from personal_web.styles.styles import *
from personal_web.constants import constants_user as const
from personal_web.components.navbar_link import navbar_link
from personal_web.components.navbar_menu_item_link import navbar_menu_item_link

def navbar():
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(
                    rx.heading(
                        const.USERNAME,
                        style = heading_navbar,
                        as_ = "h3"
                    ),
                    href = "/"
                ),
                rx.hstack(
                    navbar_link("Experencia", "experience"),
                    navbar_link("Educacion", "education"),
                    navbar_link("Proyectos", "projects"),
                    navbar_link("Sobre mi", "about_me"),
                    rx.color_mode.button(),
                    justify = "end",
                    spacing = "5",
                    align = "center"
                ),
                align_items = "center",
                justify = "between",
                padding_x = "3em",
                padding_y = "1em"
            )
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.link(
                    rx.heading(
                        const.USERNAME,
                        style = heading_navbar,
                        as_ = "h3"
                    ),
                    href = "/"
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size = 30)
                    ),
                    rx.menu.content(
                        navbar_menu_item_link("Experiencia", "experience"),
                        navbar_menu_item_link("Educacion", "education"),
                        navbar_menu_item_link("Proyectos", "projects"),
                        navbar_menu_item_link("Sobre mi", "about_me"),
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
        background_color = rx.color_mode_cond(light = "white", dark = "#111113")
    )