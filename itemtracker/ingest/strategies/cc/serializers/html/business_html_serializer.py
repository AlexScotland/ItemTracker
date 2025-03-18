import re

from bs4 import BeautifulSoup

from ingest.strategies.cc.models import BusinessProductPage
from tracking.models import Company, Item, Location, ItemStock
from tracking.factories import LocationFactory, ItemFactory, CompanyFactory, InventoryFactory


class BusinessHTMLSerializer:

    def __init__(self, page: BusinessProductPage):
        self.page = page
        self.company = self.__get_company(page.business_name)
        self.item = None

    def __get_company(self, name):
        try:
            company = Company.objects.get(name=name)
        except Company.DoesNotExist:
            company = CompanyFactory.create(name=name)
            company.save()
        return company
    
    def __get_or_create_location(self, location_name, location_ext_id):
        try:
            location = Location.objects.get(name=location_name, external_id=location_ext_id, company=self.company)
            location.external_id = location_ext_id
        except Location.DoesNotExist:
            location = LocationFactory().create(location_name, self.company, location_ext_id)
            location.save()
        return location
    
    def __get_or_create_item(self, item_name):
        try:
            item = Item.objects.get(name=item_name, company=self.company)
        except Item.DoesNotExist:
            item = ItemFactory.create(name=item_name, company=self.company, url=self.page.url)
            item.save()
        return item
    
    def __get_location_external_id(self, location_html):
        location_ext_id = location_html.find('a', {'href': re.compile(r'loc=')})
        if location_ext_id:
            location_ext_id = location_ext_id['href'].split('=')[1]
        return location_ext_id

    def __calculate_stock(self, location_html):
        location_stock = location_html.find('span', class_='stocknumber').strong.text
        if location_stock == "-":
            return 0
        return int(location_stock)
    
    def __update_stock(self, location, stock):
        try:
            item_stock = ItemStock.objects.get(item=self.item, location=location)
            item_stock.stock = stock
            item_stock.save()
        except ItemStock.DoesNotExist:
            item_stock = InventoryFactory.create(item=self.item, location=location, stock=stock)
            item_stock.save()
        except AttributeError as error_message:
            if "no attribute 'item'" in str(error_message):
                raise AttributeError(f"Item not found for {self.item.name}, did we serialize?")
            raise error_message

    def serialize_stock_by_location(self, location_divs):
        locations = []
        # Find the Location code for each div
        # we can reliably get from classes of `loc=` in href
        for location in location_divs:
            location_name = location.find('div', class_='col-9').p.text.strip()
            location_ext_id = self.__get_location_external_id(location)
            location_object = self.__get_or_create_location(location_name, location_ext_id)
            location_stock = self.__calculate_stock(location)
            self.__update_stock(location_object, location_stock)
            locations.append(location_object)
        return locations

    def __parse_html(self):
        locations = []
        for item in all_locations:
            location_name = item.find('div', class_='col-9').p.text.strip()
            stock = item.find('span', class_='stocknumber').strong.text
            if stock == "-":
                stock = 0
            locations.append(LocationFactory().create(location_name, stock))

    def serialize(self): 
        html_soup = BeautifulSoup(self.page.html, 'html.parser')
        item_name = html_soup.find('h1', class_='h3 mb-0').strong.text
        self.item = self.__get_or_create_item(item_name)
        all_locations = html_soup.find_all('div', class_='item__avail__num')
        return self.serialize_stock_by_location(all_locations)
