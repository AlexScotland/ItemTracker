from typing import List

from lib.cc.models.location import Location


class Inventory():

    def __init__(self, id, name, locations: List[Location]):
        self.id = id
        self.name = name
        self.locations = locations
