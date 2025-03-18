from tracking.models import Location


class LocationFactory():

    @staticmethod
    def create(name, company, external_id):
        return Location(
            name=name,
            external_id=external_id,
            company=company)
