from tracking.models import Location, Item, ItemStock


class InventoryFactory:

    @staticmethod
    def create(
                location: Location,
                item: Item,
                stock: int) -> Item:
        return ItemStock.objects.create(
            location=location,
            item=item,
            stock=stock)
