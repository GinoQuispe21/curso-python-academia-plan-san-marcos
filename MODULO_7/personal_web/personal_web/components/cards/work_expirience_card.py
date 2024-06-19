import reflex as rx
from personal_web.models.work_experience import WorkExpirienceModel
from personal_web.styles.styles import *
from personal_web.components.tag_software_skill import hstack_software_tags

def work_expirience_card(model):
    return rx.box(
        rx.tablet_and_desktop(
            __desktop_tablet_work_expirience(model)
        ),
        rx.mobile_only(
            __mobile_work_expirience(model)
        ),
    )

def __desktop_tablet_work_expirience(model: WorkExpirienceModel):
    return rx.hstack(
        rx.text(
            model.worked_date,
            font_size = TextSizes.BODY_HOME_TEXT.value,
            width = "20%"
        ),
        rx.vstack(
            rx.box(
                rx.text(
                    model.position_job,
                    font_size = TextSizes.HEADING_H3.value,
                    weight = "regular"
                ),
                rx.text(
                    model.company_and_city,
                    font_size = TextSizes.BODY_HOME_TEXT_MOBILE.value,
                ),
            ),
            rx.text(
                model.description_job,
                font_size = TextSizes.BODY_HOME_TEXT_MOBILE.value,
            ),
            hstack_software_tags(model.software_skills),
            spacing = "5",
            width = "80%"
        )
    )

def __mobile_work_expirience(model: WorkExpirienceModel):
        return rx.vstack(
        rx.text(
            model.worked_date,
            font_size = TextSizes.BODY_HOME_TEXT.value,
        ),
        rx.vstack(
            rx.box(
                rx.text(
                    model.position_job,
                    font_size = TextSizes.HEADING_H3.value,
                    weight = "regular"
                ),
                rx.text(
                    model.company_and_city,
                    font_size = TextSizes.BODY_HOME_TEXT_MOBILE.value,
                ),
            ),
            rx.text(
                model.description_job,
                font_size = TextSizes.BODY_HOME_TEXT_MOBILE.value,
            ),
            hstack_software_tags(model.software_skills),
            spacing = "5",
        ),
        width = "100%"
    )