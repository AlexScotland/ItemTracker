from tracking.models import Item, Company


class ItemFactory:

    @staticmethod
    def create(
                company: Company,
                name: str,
                url: str,
                external_id: str = None) -> Item:
        return Item.objects.create(
            company=company,
            external_id=external_id,
            name=name,
            url=url)
