from Product import Product


def getUrls():
    urlListFile = open("urlList", 'r')
    urls = urlListFile.read().splitlines()
    urlListFile.close()
    return urls

def deleteUrl(urlToDelete):
    urls = getUrls()
    urls = [url for url in urls if url != urlToDelete]
    writeUrls(urls)


def addUrl(urlToAdd):
    product = Product(urlToAdd)
    if not (product.name and product.price and product.currency and product.url):
        return
    urls = getUrls()
    urls.append(urlToAdd)
    writeUrls(urls)


def writeUrls(urls):
    tempUrls = []
    for url in urls:
        tempUrls.append(url + '\n')

    urlListFile = open("urlList", "w")
    urlListFile.writelines(tempUrls)
    urlListFile.close()


def getAllProducts():
    urls = getUrls()
    products = []
    for url in urls:
        product = Product(url)
        if product is None: continue
        products.append(product)

    return products


def getAllProductsAsLists():
    urls = getUrls()
    products = []
    for url in urls:
        product = Product(url)
        if product is None: continue
        products.append(product.product2List())

    return products