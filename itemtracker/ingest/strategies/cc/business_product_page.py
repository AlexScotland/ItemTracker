import requests


class BusinessProductPage():

    def __init__(self, product_id):
        self.product_id = product_id
        self.session = requests.Session()
        self.url = f"https://b2b.canadacomputers.com/product_info.php?cPath=43_557_559&item_id={product_id}"
        response = self.session.get(self.url)
        self.html = response.text
