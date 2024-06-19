import reflex as rx
from personal_web.styles.styles import *
from personal_web.constants import constants_user as const
from personal_web.components.link_icons import link_icons

def footer():
    return rx.box(
        rx.vstack(
            rx.text(
                const.FULL_NAME,
                font_size = TextSizes.HEADING_H3.value,
                weight = "bold"
            ),
            rx.link(
                rx.text(
                    const.USER_EMAIL,
                    font_size = TextSizes.LINKS_TEXT.value,
                    weight = "medium",
                    color = Color.PRIMARY.value
                ),
                href = const.URL_CONTACT_EMAIL,
                text_decoration = "none"
            ),
            rx.hstack(
                link_icons("linkedin", const.URL_LINKEDIN, 25),
                link_icons("github", const.URL_GITHUB, 25),
                link_icons("twitter", const.URL_TWITER, 25),
                spacing = "5"
            ),
            rx.box(
                rx.text(
                    "© 2024",
                    display = "inline"
                ),
                rx.link(
                    rx.color_mode_cond(
                        light =  rx.text(
                            const.USERNAME,
                            display = "inline",
                            color = Color.TEXT.value
                        ),
                        dark =  rx.text(
                            const.USERNAME,
                            display = "inline",
                            color = Color.TEXT_SECONDARY.value
                        ),
                    ),
                    href = const.URL_GITHUB,
                    is_external = True,
                    text_decoration = "none"
                ),
                rx.text(
                    ". Todos los derechos reservados.",
                    display = "inline"
                ),
                display = "inline"
            ),
            justify = "center",
            align = "center"
        ),
        border_top = border_spacer,
        width = "100%",
        padding_y = "3em"
    )