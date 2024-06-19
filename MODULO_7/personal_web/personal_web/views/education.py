import reflex as rx
from personal_web.styles.styles import *
from personal_web.components.section_header_icon import section_header_icon
from personal_web.models.mock_data_manager import MockDataManager
from personal_web.components.cards.education_card import education_card

def education():
    return rx.box(
        section_header_icon(
            "graduation-cap",
            "Educacion"
        ),
        __body_hstack_education(),
        id = "education"
    )

def __body_hstack_education():
    list_objects = MockDataManager.get_education_models()
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                *[
                    education_card(model)
                    for model in list_objects
                ],
                spacing = "7",
                margin_top = "3em"
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                *[
                    education_card(model)
                    for model in list_objects
                ],
                spacing = "7",
                margin_top = "3em"
            )
        )
    )