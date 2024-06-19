import reflex as rx
from personal_web.styles.styles import *
from personal_web.components.section_header_icon import section_header_icon
from personal_web.models.mock_data_manager import MockDataManager
from personal_web.components.cards.work_expirience_card import work_expirience_card

def laboral_expirience():
    return rx.box(
        section_header_icon(
            "briefcase-business",
            "Experiencia"
        ),
        __body_vstack_expirience(),
        id = "experience",
    )

def __body_vstack_expirience():
    list_objets = MockDataManager.get_work_expirience_models()
    return rx.vstack(
        *[
            work_expirience_card(model)
            for model in list_objets
        ],
        margin_top = "4em",
        spacing = "9"
    )