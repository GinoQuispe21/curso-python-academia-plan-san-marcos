import reflex as rx
from personal_web.views.navbar import navbar
from personal_web.views.welcome_home import welcome_home
from personal_web.views.laboral_expirience import laboral_expirience
from personal_web.views.education import education
from personal_web.views.projects import projects
from personal_web.views.about_me import about_me
from personal_web.views.footer import footer

def index():
    return rx.box(
        navbar(),
        rx.vstack(
            welcome_home(),
            laboral_expirience(),
            education(),
            projects(),
            about_me(),
            align = "center",
            justify = "center",
            margin_x = "8.5vw",
            spacing = "9",
            margin_bottom = "4em"
        ),
        footer(),
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