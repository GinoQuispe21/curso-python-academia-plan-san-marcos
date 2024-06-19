import reflex as rx
from personal_web.styles.styles import *
from personal_web.constants import constants_user as const
from personal_web.components.link_icons import link_icons
from personal_web.components.buttons import main_button, secondary_button

def welcome_home():
    return rx.center(
        rx.desktop_only(
            __dektop_welcome_home()
        ),
        rx.tablet_only(
            __table_welcome_home()
        ),
        rx.mobile_only(
            __mobile_welcome_home()
        ),
        min_height = "70vh",
    )

def __dektop_welcome_home():
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.heading(
                    const.FULL_NAME,
                    font_size = TextSizes.HEADING_H1.value,
                    as_ = "h1",
                    line_height = "1.2em"
                ),
                rx.text(
                    const.PROFESSION_PLACE,
                    font_size = TextSizes.HEADING_H2.value,
                    weight = "regular"
                ),
                rx.text(
                    const.HOME_SHORT_DESCRIPTION,
                    font_size = TextSizes.BODY_HOME_TEXT.value,
                    as_ = "p"
                ),
                rx.hstack(
                    link_icons("linkedin", const.URL_LINKEDIN, 35),
                    link_icons("github", const.URL_GITHUB, 35),
                    link_icons("twitter", const.URL_TWITER, 35),
                    spacing = "5"
                ),
                rx.hstack(
                    main_button(
                        "download",
                        "Descargar CV",
                        const.URL_PUBLIC_CV,
                        "4"
                    ),
                    secondary_button(
                        "mail",
                        "Contactame",
                        const.URL_CONTACT_EMAIL,
                        "4"
                    ),
                    spacing = "5"
                )
            ),
            rx.image(
                src = "/personal/person.png",
                width = "auto",
                height = "22vw",
                border_radius = "30px"
            ),
            align = "center",
            spacing = "7"
        )
    )

def __table_welcome_home():
    return rx.box(
        rx.vstack(
            rx.image(
                src = "/personal/person.png",
                width = "auto",
                height = "270px",
                border_radius = "30px"
            ),
            rx.vstack(
                rx.heading(
                    const.FULL_NAME,
                    font_size = TextSizes.HEADING_H1.value,
                    as_ = "h1",
                    line_height = "1.2em"
                ),
                rx.text(
                    const.PROFESSION_PLACE,
                    font_size = TextSizes.HEADING_H2.value,
                    weight = "regular"
                ),
                rx.text(
                    const.HOME_SHORT_DESCRIPTION,
                    font_size = TextSizes.BODY_HOME_TEXT.value,
                    as_ = "p"
                ),
                rx.hstack(
                    link_icons("linkedin", const.URL_LINKEDIN, 35),
                    link_icons("github", const.URL_GITHUB, 35),
                    link_icons("twitter", const.URL_TWITER, 35),
                    spacing = "5"
                ),
                rx.hstack(
                    main_button(
                        "download",
                        "Descargar CV",
                        const.URL_PUBLIC_CV,
                        "4"
                    ),
                    secondary_button(
                        "mail",
                        "Contactame",
                        const.URL_CONTACT_EMAIL,
                        "4"
                    ),
                    spacing = "6"
                )
            ),
            align = "center",
            spacing = "7",
        ),
        margin_top = "3em"
    )

def __mobile_welcome_home():
    return rx.box(
        rx.vstack(
            rx.image(
                src = "/personal/person.png",
                width = "auto",
                height = "270px",
                border_radius = "30px"
            ),
            rx.vstack(
                rx.heading(
                    const.FULL_NAME,
                    font_size = TextSizes.HEADING_H1_MOBILE.value,
                    as_ = "h1",
                    line_height = "1.2em",
                    text_align = "center"
                ),
                rx.text(
                    const.PROFESSION_PLACE,
                    font_size = TextSizes.HEADING_H2_MOBILE.value,
                    weight = "regular",
                    text_align = "center",
                    width = "100%"
                ),
                rx.text(
                    const.HOME_SHORT_DESCRIPTION,
                    font_size = TextSizes.BODY_HOME_TEXT_MOBILE.value,
                    as_ = "p"
                ),
                rx.hstack(
                    link_icons("linkedin", const.URL_LINKEDIN, 25),
                    link_icons("github", const.URL_GITHUB, 25),
                    link_icons("twitter", const.URL_TWITER, 25),
                    spacing = "5",
                    justify = "center",
                    align = "center",
                    width = "100%"
                ),
                rx.vstack(
                    main_button(
                        "download",
                        "Descargar CV",
                        const.URL_PUBLIC_CV,
                        "4"
                    ),
                    secondary_button(
                        "mail",
                        "Contactame",
                        const.URL_CONTACT_EMAIL,
                        "4"
                    ),
                    spacing = "4",
                    justify = "center",
                    align = "center",
                    width = "100%"
                )
            ),
            align = "center",
            spacing = "7"
        ),
        margin_top = "3em"
    )