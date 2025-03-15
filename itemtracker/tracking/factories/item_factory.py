from tracking.models import Location, Item


class ItemFactory:

    @staticmethod
    def create(location: Location,
                    stock: int,
                    name: str,
                    url: str,
                    external_id: str = None) -> Item:
        return Item.objects.create(
            location=location,
            stock=stock,
            external_id=external_id,
            name=name,
            url=url)
