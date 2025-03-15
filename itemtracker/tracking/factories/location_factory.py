from lib.cc.models.location import Location


class LocationFactory():

    def create(self, name, stock):
        return Location(name, stock)
