from enum import Enum
import reflex as rx

class Color(Enum):

    PRIMARY = "#19C28C"
    SECONDARY = "#CEF1E6"
    BACKGROUND = "white"
    BACKGROUND_CONTENT = "#F7F6F6"
    TEXT = "black"
    TEXT_SECONDARY = "white"

class TextSizes(Enum):

    HEADING_H1 = "3em"
    HEADING_H2 = "2em"
    HEADING_H3 = "1.7em"
    LINKS_TEXT = "1.2em"
    BODY_HOME_TEXT = "1.5em"
    SECTION_HEADING = "2.5em"
    CARD_HEADER = "1.2em"
    CARD_BODY = "1em"

    HEADING_H1_MOBILE = "2em"
    HEADING_H2_MOBILE = "1.5em"
    HEADING_H3_MOBILE = "1.3em"
    BODY_HOME_TEXT_MOBILE = "1.2em"

heading_navbar = dict(
    weight = "bold",
    align = "center",
    color = Color.PRIMARY.value,
    font_size = TextSizes.HEADING_H3.value,
    cursor = "pointer"
)

text_could_hover = {
    "font_size": TextSizes.LINKS_TEXT.value,
    "font_weight": "regular",
    "_hover": {
        "color": Color.PRIMARY.value,
        "font_weight": "bold"
    },
    "cursor": "pointer"
}

color_border = rx.color_mode_cond(light = Color.BACKGROUND_CONTENT.value, dark = "#1F1F22")
border_spacer = f"1px solid {color_border}"

button_secondary_hover = {
    "color": rx.color_mode_cond(light = "black", dark = "white"),
    "_hover": {
        "font_weight": "bold",
        "color": Color.TEXT_SECONDARY.value,
        "background_color": Color.PRIMARY.value
    },
    "cursor": "pointer"
}

main_button_style = dict(
    color = Color.TEXT_SECONDARY.value,
    background_color = Color.PRIMARY.value,
    border_radius = "10px",
    font_weight = "bold",
    cursor = "pointer"
)

secondary_button_style = dict(
    color = Color.PRIMARY.value,
    background_color = Color.BACKGROUND.value,
    border = f"3px solid {Color.PRIMARY.value}",
    border_radius = "10px",
    font_weight = "bold",
    _hover = button_secondary_hover
)