from lib.cc.models.inventory import Inventory


class InventoryFactory():

    def create(self, id, name, locations):
        return Inventory(id, name, locations)
