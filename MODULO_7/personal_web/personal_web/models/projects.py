
class ProjectModel:

    def __init__(
            self,
            src_image: str,
            proyect_title: str,
            description: str,
            url_github: str,
            url_proyect: str,
            *software_skills: str,
    ):
        self.src_image =  src_image
        self.proyect_title = proyect_title
        self.software_skills = software_skills
        self.description  = description
        self.url_github = url_github
        self.url_proyect = url_proyect