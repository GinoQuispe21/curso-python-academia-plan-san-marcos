import reflex as rx

class CounterState(rx.State):
    count:str = 0
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1

def index() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.button(
                "Disminuir",
                on_click = CounterState.decrement,
                color_scheme = "ruby"
            ),
            rx.heading(
                CounterState.count,
                font_size = "2em"
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

app = rx.App()
app.add_page(index)