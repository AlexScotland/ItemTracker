import re

from bs4 import BeautifulSoup

from ingest.strategies.cc.models import BusinessProductPage
from tracking.models import Company, Item, Location
from tracking.factories import LocationFactory, ItemFactory, CompanyFactory


class BusinessHTMLSerializer:

    def __init__(self, page: BusinessProductPage):
        self.page = page
        self.company = self.__get_company(page.business_name)

    def __get_company(self, name):
        try:
            company = Company.objects.get(name=name)
        except Company.DoesNotExist:
            company = CompanyFactory.create(name=name)
            company.save()
        return company

    def serialize_locations(self, location_divs):
        locations = []
        # Find the Location code for each div
        # we can reliably get from classes of `loc=` in href
        for location in location_divs:
            location_ext_id = location.find('a', {'href': re.compile(r'loc=')})
            if location_ext_id:
                location_ext_id = location_ext_id['href'].split('=')[1]
            location_name = location.find('div', class_='col-9').p.text.strip()
            location_stock = location.find('span', class_='stocknumber').strong.text
            if location_stock == "-":
                location_stock = 0
            try:
                location_obj = Location.objects.get(name=location_name, company=self.company)
                location_obj.stock = location_stock
            except Location.DoesNotExist:
                location_obj = LocationFactory().create(location_name, self.company, location_ext_id, location_stock)
            finally:
                location_obj.save()
            locations.append(location_obj)
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
        all_locations = html_soup.find_all('div', class_='item__avail__num')
        locations = self.serialize_locations(all_locations)
        try:
            item = Item.objects.get(name=item_name, location__company=self.company)
        except Item.DoesNotExist:
            item = ItemFactory().create(self.company, item_name, self.page.url, self.page.external_id)
            item.save()
