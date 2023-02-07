from Product import Product



class FileService:

    def __init__(self):
        self.listOfProductsAsLists = []
        self.listOfProducts = []
        self.urls = []


    def getUrls(self):
        if self.urls:
            return self.urls
        urlListFile = open("urlList", 'r')
        urls = urlListFile.read().splitlines()
        urlListFile.close()

        self.urls = urls
        return self.urls

    def deleteUrl(self, urlToDelete):
        self.urls = [url for url in self.urls if url != urlToDelete]
        self.listOfProducts = [product for product in self.listOfProducts if product.url != urlToDelete]
        self.listOfProductsAsLists = [product for product in self.listOfProductsAsLists if product[3] != urlToDelete]
        self.writeUrls()


    def addUrl(self, urlToAdd):
        product = Product(urlToAdd)
        if not (product.name and product.price and product.currency and product.url):
            return

        self.listOfProducts.append(product)
        self.listOfProductsAsLists.append(product.product2List())
        self.urls.append(urlToAdd)
        self.writeUrls()


    def writeUrls(self):
        tempUrls = []
        for url in self.urls:
            tempUrls.append(url + '\n')

        urlListFile = open("urlList", "w")
        urlListFile.writelines(tempUrls)
        urlListFile.close()


    def getAllProducts(self):
        if self.listOfProducts:
            return self.listOfProducts
        urls = self.getUrls()
        products = []
        productsAsLists = []
        for url in urls:
            product = Product(url)
            if product is None: continue
            products.append(product)
            productsAsLists.append(product.product2List())
        self.listOfProducts = products
        self.listOfProductsAsLists = productsAsLists
        return self.listOfProducts


    def getAllProductsAsLists(self):
        if self.listOfProductsAsLists:
            return self.listOfProductsAsLists

        urls = self.getUrls()
        productsAsLists = []
        products = []
        for url in urls:
            product = Product(url)
            if product is None: continue
            products.append(product)
            productsAsLists.append(product.product2List())
        self.listOfProducts = products
        self.listOfProductsAsLists = productsAsLists

        return self.listOfProductsAsLists

fileService = FileService()