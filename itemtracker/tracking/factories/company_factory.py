from tracking.models import Company


class CompanyFactory():

    @staticmethod
    def create(name):
        return Company(name=name)
