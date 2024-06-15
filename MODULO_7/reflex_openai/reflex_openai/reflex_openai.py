"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from reflex_openai.styles import *
from reflex_openai.state import ChatBotState

def qa(
        question: str, 
        answer: str
    ):
    return rx.box(
        rx.box(
            rx.text(
                question,
                style = question_style
            ),
            text_align = "right"
        ),
        rx.box(
            rx.text(
                answer,
                style = answer_style
            ),
            text_align = "left",
        ),
        margin_y = "1em"
    )

def chat(): 
    return rx.box(
        rx.foreach(
            ChatBotState.chat_history,
            lambda messags: qa(messags[0], messags[1])
        )
    )

def action_bar():
    return rx.hstack(
        rx.input(
            value = ChatBotState.question,
            placeholder = "Realice una pregunta a la IA",
            width = "100%",
            style = input_style,
            on_change = ChatBotState.set_question
        ),
        rx.button(
            "Preguntar",
            style = button_style,
            on_click = ChatBotState.answer
        ),
        justify = "center",
        width = "100%"
    )

def index() -> rx.Component:
    return rx.container(
        rx.box(
            chat(),
            action_bar(),
            background_color = "lightgreen",
            padding = "1em"
        ),
        background_color = "lightblue",
        height = "100vh"
    )


app = rx.App()
app.add_page(index)
