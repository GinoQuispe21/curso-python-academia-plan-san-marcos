import reflex as rx
from personal_web.styles.styles import *
from personal_web.components.section_header_icon import section_header_icon
from personal_web.components.paragraph_normal_and_bold import paragraph_normal_and_bold

def about_me():
    return rx.center(
        rx.desktop_only(
            __dektop_about_me()
        ),
        rx.mobile_and_tablet(
            __mobile_about_me()
        ),
        id = "about_me"
    )

def __dektop_about_me():
    return rx.box(
        section_header_icon(
            "user",
            "Sobre mi"
        ),
        rx.hstack(
            rx.vstack(
                paragraph_normal_and_bold(
                    "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, ",
                    ":bold:eaque ipsa quae ab illo inventore veritatis et quasi ",
                    "architecto beatae vitae dicta sunt explicabo."
                ),
                paragraph_normal_and_bold(
                    "Nemo enim ipsam voluptatem quia",
                    ":bold:voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur ",
                    "magni dolores eos qui ratione voluptatem sequi nesciunt."
                ),
                paragraph_normal_and_bold(
                    "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, ",
                    ":bold:consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut",
                    "labore et dolore magnam aliquam quaerat voluptatem."
                ),
                width = "75%"
            ),
            rx.flex(
                rx.image(
                    src = "/personal/about_me.jpg",
                    width = "auto",
                    height = "250px",
                    border_radius = "30px"
                ),
                width = "25%",
                justify = "center",
                align = "center"
            ),
            width = "100%",
            margin_top = "4em",
            align = "center"
        ),
        width = "100%",
    )


def __mobile_about_me():
    return rx.box(
        section_header_icon(
            "user",
            "Sobre mi"
        ),
        rx.vstack(
            rx.flex(
                rx.image(
                    src = "/personal/about_me.jpg",
                    width = "auto",
                    height = "200px",
                    border_radius = "30px"
                ),
                justify = "center",
                align = "center"
            ),
            rx.vstack(
                paragraph_normal_and_bold(
                    "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, ",
                    ":bold:eaque ipsa quae ab illo inventore veritatis et quasi ",
                    "architecto beatae vitae dicta sunt explicabo."
                ),
                paragraph_normal_and_bold(
                    "Nemo enim ipsam voluptatem quia",
                    ":bold:voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur ",
                    "magni dolores eos qui ratione voluptatem sequi nesciunt."
                ),
                paragraph_normal_and_bold(
                    "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, ",
                    ":bold:consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut",
                    "labore et dolore magnam aliquam quaerat voluptatem."
                ),
            ),
            width = "100%",
            margin_top = "4em",
            align = "center",
            spacing = "6"
        ),
        width = "100%",
    )
