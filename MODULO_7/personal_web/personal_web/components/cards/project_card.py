import reflex
from personal_web.models.projects import ProjectModel
from personal_web.styles.styles import *
from personal_web.components.tag_software_skill import hstack_software_tags
from personal_web.components.buttons import main_button, secondary_button

def project_card(model: ProjectModel):
    return rx.box(
        rx.desktop_only(
            __desktop_project_card(model)
        ),
        rx.mobile_and_tablet(
            __mobile_tablet_project_card(model)
        )
    )

def __desktop_project_card(model: ProjectModel):
    return rx.hstack(
        rx.image(
            src = model.src_image,
            width = "550px",
            height = "317px",
            border_radius = "15px"
        ),
        rx.flex(
            rx.vstack(
                rx.text(
                    model.proyect_title,
                    font_size = TextSizes.HEADING_H3.value,
                    weight = "bold"
                ),
                hstack_software_tags(model.software_skills),
                rx.text(
                    model.description,
                    font_size = TextSizes.HEADING_H3.value,
                ),
                rx.hstack(
                    main_button(
                        "github",
                        "Codigo",
                        model.url_github,
                        size_str = "3"
                    ),
                    main_button(
                        "link",
                        "Visitar",
                        model.url_proyect,
                        size_str = "3"
                    ),
                    spacing = "6"
                )
            ),
        ),
        spacing = "9",
        align = "center",
    )

def __mobile_tablet_project_card(model: ProjectModel):
    return rx.vstack(
        rx.image(
            src = model.src_image,
            width = "100%",
            height = "auto",
            border_radius = "15px"
        ),
        rx.flex(
            rx.vstack(
                rx.text(
                    model.proyect_title,
                    font_size = TextSizes.HEADING_H3.value,
                    weight = "bold"
                ),
                hstack_software_tags(model.software_skills),
                rx.text(
                    model.description,
                    font_size = TextSizes.HEADING_H3.value,
                ),
                rx.hstack(
                    main_button(
                        "github",
                        "Codigo",
                        model.url_github,
                        size_str = "3"
                    ),
                    main_button(
                        "link",
                        "Visitar",
                        model.url_proyect,
                        size_str = "3"
                    ),
                    spacing = "6"
                )
            ),
        ),
        spacing = "3",
        align = "center",
    )