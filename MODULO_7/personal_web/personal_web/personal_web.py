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
            margin_x = "8.5vw"
        ),
        width = "100%"
    )

app = rx.App(
    theme= rx.theme(
        appearance = "light"
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap",
    ],
    style = {
        "font_family": "Montserrat, sans-serif",
        "font_size": "13px"
    }
)
app.add_page(index, title = "Portafolio de Gino Quispe Calixto")