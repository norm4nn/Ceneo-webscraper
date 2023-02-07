from abc import ABC, abstractmethod

import FileService
import Table
import InputElement
import GUI


class AbstractScene(ABC):
    def __init__(self, root):
        self.root = root
        self.elements = []

    def clear(self):
        widgets = self.root.grid_slaves()

        for widget in widgets:
            widget.destroy()

    def rebuild(self):
        self.clear()

        for element in self.elements:
            element.create()

    def addElement(self, element):
        self.elements.append(element)

class ListScene(AbstractScene):
    freeRowsOnTop = 1

    def __init__(self, root):
        super().__init__(root)

        self.addElement(Table.SortingTable(self, FileService.fileService.getAllProductsAsLists(), ["name", "price", "currency"]))
        self.addElement(InputElement.ProductInput(self))

    def getInputRow(self):
        return self.freeRowsOnTop + len(FileService.fileService.getAllProductsAsLists())