class WorkExpirienceModel:

    def __init__(
            self, 
            worked_date: str,
            position_job: str,
            company_and_city: str,
            description_job: str,
            *software_skills: str,
    ):
        self.worked_date =  worked_date
        self.position_job = position_job
        self.company_and_city = company_and_city
        self.description_job  = description_job
        self.software_skills = software_skills