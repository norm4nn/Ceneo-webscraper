import getAllProducts
import GUI
import fileOperations


if __name__ == '__main__':
    # fileOperations.addUrl("https://www.ceneo.pl/45498987")

    products = getAllProducts.getAllProducts()

    GUI.run(products)

