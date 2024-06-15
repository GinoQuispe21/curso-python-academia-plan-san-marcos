import reflex as rx
from personal_web.views.navbar import navbar
from personal_web.views.welcome_home import welcome_home

def index():
    return rx.box(
        navbar(),
        rx.vstack(
            welcome_home(),
            align = "center",
            justify = "center",
            margin_x = "5vw"
        ),
        width = "100%"
    )

app = rx.App(
    style = {
        "font_size": "13px"
    }
)
app.add_page(index)