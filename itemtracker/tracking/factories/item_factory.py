from tracking.models import Location, Item, Company


class ItemFactory:

    @staticmethod
    def create(
                location: Location,
                name: str,
                url: str,
                external_id: str = None) -> Item:
        return Item.objects.create(
            location=location,
            external_id=external_id,
            name=name,
            url=url)
