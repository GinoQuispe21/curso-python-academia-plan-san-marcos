import reflex as rx
from .states import CounterState
import requests

def index_counter_buttons() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.button(
                "Disminuir",
                on_click = CounterState.decrement,
                color_scheme = "ruby"
            ),
            rx.heading(
                CounterState.count,
                font_size = "2em",
                as_= "h1"
            ),
            rx.button(
                "Aumentar",
                on_click = CounterState.increment,
                color_scheme = "grass"
            ),
            min_height = "90vh",
            justify = "center",
            align = "center"
        ),
        background_color = "lightgray",
    )   


class GitHubState(rx.State):

    url: str = "https://github.com/reflex-dev"
    profile_image: str = "https://avatars.githubusercontent.com/u/104714959"

    def set_profile_image(self, username: str):
        if username == "": return
        data = requests.get(
            f"https://api.github.com/users/{username}"
        ).json()
        self.url = data["url"]
        self.profile_image = data["avatar_url"]
        #print(data)

def index():
    return rx.hstack(
        rx.link(
            rx.avatar(
                src = GitHubState.profile_image,
                size = "9"
            ),
            href = GitHubState.url,
            is_external = True
        ),
        rx.input(
            placeholder = "TU usuaruio de Github",
            on_blur = GitHubState.set_profile_image,
            size = "3"
        ),
        spacing = "5",
        justify = "center", # alinearlos de manera horizontal
        align = "center", # alinearlos de manera vertical
        min_height = "100vh" # viewport/ size de la pantalla que considere el total
    )

app = rx.App()
app.add_page(index)