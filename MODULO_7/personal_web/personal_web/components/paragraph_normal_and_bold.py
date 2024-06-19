import reflex as rx
from personal_web.styles.styles import *

def paragraph_normal_and_bold(*args: str):
    """
    *args: oraciones del parrafo
    - 1. iniciar parrafo con bold
        Ejm: :bold:lorem ipsum ... (para negritas)
    - 2. iniciar parrafo sin bold
        Ejm: lorem ipsum ...(texto normal)
    """
    return rx.box(
        *[
            bold_text(arg)
            if (
                arg.startswith(":bold:")
            ) else 
            normal_text(arg)
            for arg in args
        ],
        display = "inline"
    )

def normal_text(text: str):
    return rx.text(
        text,
        display = "inline",
        font_size = TextSizes.BODY_HOME_TEXT.value
    )

def bold_text(text: str):
    return rx.text(
        text[6:],
        weight = "bold",
        display = "inline",
        color = Color.PRIMARY.value,
        font_size = TextSizes.BODY_HOME_TEXT.value
    )