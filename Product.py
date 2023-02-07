from bs4 import BeautifulSoup
import requests

headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

class Product:


    def __init__(self, url):
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'lxml')
        mainProduct = soup.find('article', class_='product-top')

        if mainProduct is None: return

        name = mainProduct.find('h1').text
        value = mainProduct.find('span', class_='value').text
        penny = mainProduct.find('span', class_='penny').text
        priceS = value + penny
        priceS = priceS.replace(',', '.')
        priceS = priceS.replace(' ', '')
        priceF = float(priceS)
        currency = mainProduct.find('span', class_='price-format nowrap').text[-2:]

        self.name = name
        self.price = priceF
        self.currency = currency
        self.url = url

    def product2List(self):
        return [self.name, self.price, self.currency, self.url]