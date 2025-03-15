from bs4 import BeautifulSoup

from lib.cc.wrappers.business_product_page import BusinessProductPage
from lib.cc.factories.location_factory import LocationFactory
from lib.cc.factories.inventory_factory import InventoryFactory


class BusinessHTMLSerializer:

    def serialize(self, product_page: BusinessProductPage):
        html_soup = BeautifulSoup(product_page.html, 'html.parser')
        name = html_soup.find('h1', class_='h3 mb-0').strong.text
        all_locations = html_soup.find_all('div', class_='item__avail__num')
        locations = []
        for item in all_locations:
            location_name = item.find('div', class_='col-9').p.text.strip()
            stock = item.find('span', class_='stocknumber').strong.text
            if stock == "-":
                stock = 0
            locations.append(LocationFactory().create(location_name, stock))
        return InventoryFactory().create(product_page.product_id, name, locations)

