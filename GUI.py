import tkinter as tk
import tkmacosx as tkmac

import fileOperations
import getAllProducts

root = tk.Tk()
root.geometry("600x300")
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
freeRowsOnTop = 1

def addRecord(url):
    fileOperations.addUrl(url)
    products = getAllProducts.getAllProducts()
    buildList(products)

def eraseRecord(url):
    fileOperations.deleteUrl(url)
    products = getAllProducts.getAllProducts()
    buildList(products)

def buildList(products):
    widgets = root.grid_slaves()
    for widget in widgets:
        widget.destroy()


    idLabel = tk.Label(root, text="ID")
    nameLabel = tk.Label(root, text="Nazwa")
    priceLabel = tk.Label(root, text="Cena")
    idLabel.grid(row=0, column=0, pady=10, padx=5)
    nameLabel.grid(row=0, column=1)
    priceLabel.grid(row=0, column=2)

    for i, product in enumerate(products):
        productIdLabel = tk.Label(root, text=str(i + 1))
        productNameLabel = tk.Label(root, text=product.name)
        productPriceLabel = tk.Label(root, text="{:.2f}".format(product.price))
        productCurrencyLabel = tk.Label(root, text=product.currency)
        deleteButton = tkmac.Button(root,bg='red', fg='white', width=30, text='X', command=lambda p=product: eraseRecord(p.url))

        productIdLabel.grid(row=i + freeRowsOnTop, column=0)
        productNameLabel.grid(row=i + freeRowsOnTop, column=1)
        productPriceLabel.grid(row=i + freeRowsOnTop, column=2)
        productCurrencyLabel.grid(row=i + freeRowsOnTop, column=3)
        deleteButton.grid(row=i + freeRowsOnTop, column=4, padx=5)

    rowOfAddingWidgets = freeRowsOnTop + len(products)
    urlInput = tk.Entry(root)
    addButton = tkmac.Button(root,bg='green', fg='white', text='Dodaj url', command=lambda: addRecord(urlInput.get()))
    urlInput.grid(row=rowOfAddingWidgets, column=1, pady=20)
    urlInput.focus()
    addButton.grid(row=rowOfAddingWidgets, column=2)





def run(products):

    buildList(products)
    root.mainloop()