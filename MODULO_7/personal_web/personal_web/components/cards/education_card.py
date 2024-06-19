import reflex as rx
from personal_web.models.education import EducationalModel, EducationalType
from personal_web.styles.styles import *

def education_card(model: EducationalModel):
    return rx.card(
        rx.vstack(
            rx.icon(
                __get_icon_by_education_type(model.education_type),
                size = 30
            ),
            rx.text(
                model.study_subject,
                font_size = TextSizes.HEADING_H3.value,
                color = Color.PRIMARY.value,
                weight = "bold"
            ),
            rx.text(
                model.education_type,
                font_size = TextSizes.CARD_HEADER.value,
                weight = "regular"
            ),
            rx.text(
                model.range_years,
                font_size = TextSizes.CARD_BODY.value,
            ),
            rx.text(
                model.description,
                font_size = TextSizes.CARD_BODY.value,
                text_align = "center"
            ),
            align = "center",
            justify = "center",
            padding_y = "2em"
        )
    )

def __get_icon_by_education_type(type: EducationalType):
    if type == EducationalType.UNIVERSITY.value:
        return "university"
    elif type == EducationalType.LENGAGUE.value:
        return "languages"
    elif type == EducationalType.CERTIFICATE.value:
        return "file-badge"
    else:
        return "file-badge"