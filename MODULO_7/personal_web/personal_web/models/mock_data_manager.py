from personal_web.models.work_experience import WorkExpirienceModel
from personal_web.models.education import EducationalModel, EducationalType
from personal_web.models.projects import ProjectModel

class MockDataManager:

    @staticmethod
    def get_work_expirience_models():
        work_expirience_models_list = [
            WorkExpirienceModel(
                "2023 - Actualidad",
                "Desarrollador de Software Python",
                "Empresa SAC - Lima, Peru",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
                "Python", "Tkinter", "Sqlite3", "Django"
            ),
            WorkExpirienceModel(
                "2022 - 2023",
                "Desarrollador Mobile iOS",
                "Empresa SAC - Trujillo, Peru",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
                "Swift", "UIKit", "CoreData", "ARKit"
            ),
            WorkExpirienceModel(
                "2020 - 2022",
                "Desarrollador de Software Java",
                "Empresa SAC - Lima, Peru",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
                "Java", "Spring Boot"
            ),
        ]
        return work_expirience_models_list

    @staticmethod
    def get_education_models():
        education_models_list = [
            EducationalModel(
                education_type = EducationalType.UNIVERSITY.value,
                study_subject = "Bachiller Ing. de Software",
                educational_entity = "UPC",
                range_years = "2018-2022",
                description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  incididunt ut labore et dolore magna magna magna magna magna aliqua. "
            ),
            EducationalModel(
                education_type = EducationalType.LENGAGUE.value,
                study_subject = "Ingles Avanzado",
                educational_entity = "ICPNA",
                range_years = "2018-2021",
                description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  incididunt ut labore et dolore magna magna magna magna magna aliqua. "
            ),
            EducationalModel(
                education_type = EducationalType.CERTIFICATE.value,
                study_subject = "Python for everybody",
                educational_entity = "UMich",
                range_years = "2022",
                description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  incididunt ut labore et dolore magna magna magna magna magna aliqua. "
            ),
        ]
        return education_models_list

    @staticmethod
    def get_projectS_models():
        project_models_list = [
            ProjectModel(
                "/projects/project_1.png",
                "Speedplaner - Landing page de aplicacion movil",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
                "https://github.com/GinoQuispe21/Landing-Page-SpeedPlanner---SI652",
                "https://ginoquispe21.github.io/Landing-Page-SpeedPlanner---SI652/",
                "HTML", "Css"
            ),
            ProjectModel(
                "/projects/project_2.png",
                "GinoExclusive - Landing page para empresa de venta de ropa deportiva",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
                "https://github.com/GinoQuispe21/Gino-Exclusive-LandingPage/",
                "https://ginoquispe21.github.io/Gino-Exclusive-LandingPage/",
                "HTML", "Css", "Javascript"
            ),
            ProjectModel(
                "/projects/project_3.png",
                "ToDo list - Web App para organizar tareas",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
                "https://github.com/GinoQuispe21/django-organizer-project",
                "https://django-organizer-project.onrender.com/",
                "Python", "Django", "Html", "Css", "PostgreSQL"
            )
        ]
        return project_models_list