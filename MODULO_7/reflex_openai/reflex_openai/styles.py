import reflex as rx

shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"

message_style = dict(
    padding = "1em",
    border_radix = "5px",
    margin_y = "0.5em",
    box_shadow = shadow,
    display = "inline-block",
    max_width = "30em"
)

question_style = message_style | dict(
    margin_left = chat_margin,
    background_color = rx.color("gray", 1)
)

answer_style = message_style | dict(
    margin_right = chat_margin,
    background_color = rx.color("pink", 5)
)

input_style = dict(
    border_width = "1px",
    padding = "0.1em",
    box_shadow = shadow
)

button_style = dict(
    background_color = rx.color("pink", 10),
    box_shadow = shadow
)