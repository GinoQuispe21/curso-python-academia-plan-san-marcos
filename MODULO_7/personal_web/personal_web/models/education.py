from enum import Enum

class EducationalType(Enum):

    UNIVERSITY = "university"
    LENGAGUE = "lenguahge"
    CERTIFICATE = "certificate"
    PUBLICATION = "publication"

class EducationalModel:

    def __init__(
            self,
            education_type: EducationalType,
            study_subject: str,
            educational_entity: str,
            range_years: str,
            description: str,
    ):
        self.education_type =  education_type
        self.study_subject = study_subject
        self.educational_entity = educational_entity
        self.range_years  = range_years
        self.description = description