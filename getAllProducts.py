import fileOperations
from ProductClass import Product


def getAllProducts():
    urls = fileOperations.getUrls()
    products = []
    for url in urls:
        product = Product(url)
        if product is None: continue
        products.append(product)

    return products

