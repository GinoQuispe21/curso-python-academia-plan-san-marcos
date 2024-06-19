import reflex as rx
from personal_web.styles.styles import *
from personal_web.components.section_header_icon import section_header_icon
from personal_web.models.mock_data_manager import MockDataManager
from personal_web.components.cards.project_card import project_card

def projects():
    return rx.box(
        section_header_icon(
            "code",
            "Proyectos"
        ),
        __body_vstack_projects(),
        id = "projects"
    )

def __body_vstack_projects():
    list_objects = MockDataManager.get_projectS_models()
    return rx.vstack(
        *[
            project_card(model)
            for model in list_objects
        ],
        spacing = "9",
        margin_top = "4em"
    )