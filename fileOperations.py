import ProductClass


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
    product = ProductClass.Product(urlToAdd)
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