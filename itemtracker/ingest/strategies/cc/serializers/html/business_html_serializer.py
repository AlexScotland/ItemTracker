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
        for item in location_divs:
            location_name = item.find('div', class_='col-9').p.text.strip()
            stock = item.find('span', class_='stocknumber').strong.text
            if stock == "-":
                stock = 0
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
        name = html_soup.find('h1', class_='h3 mb-0').strong.text
        all_locations = self.html_soup.find_all('div', class_='item__avail__num')

        return InventoryFactory().create(product_page.product_id, name, locations)
