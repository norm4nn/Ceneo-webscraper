import tkinter as tk
import tkmacosx as tkmac
from abc import ABC, abstractmethod

import SceneElement
import fileOperations
from Row import ProductRow

class AbstractSortingTable(SceneElement.AbstractSceneElement):


    def __init__(self, scene, data, columnNames,  sortByColumnID = 0, descending = False):
        super().__init__(scene)
        self.scene = scene
        self.data = data
        self.width = len(columnNames) + 1
        self.columnNames = columnNames
        self.sortByColumnID = sortByColumnID
        self.descending = descending

        for i, _ in enumerate(self.columnNames):
            self.scene.root.columnconfigure(i + 1, weight=1)


    def create(self):
        self.reloadData()
        self.buildTable()

    def changeSorting(self, newSorting):
        print(newSorting)
        self.sortByColumnID = newSorting//2
        self.descending = (newSorting)%2
        self.scene.rebuild()


    def sort(self):
        self.data.sort(key=lambda x: x[self.sortByColumnID], reverse=self.descending)
        print(self.sortByColumnID,self.descending, self.data)

    def buildTable(self):
        idLabel = tk.Label(self.scene.root, text="ID")
        idLabel.grid(row=0, column=0, pady=10, padx=5)

        for i, name in enumerate(self.columnNames):
            columnNameLabel = tk.Label(self.scene.root, text=name)
            columnNameLabel.grid(row=0, column=i + 1, pady=10, padx=5)

            upArrowButton = tkmac.Button(self.scene.root, width=20, height=20, text=u"\u2191",
                                              command=lambda x=i: self.changeSorting(2*x))
            upArrowButton.grid(row=0, column= i + 1, pady=10, padx=5, sticky='e')

            downArrowButton = tkmac.Button(self.scene.root, width=20, height=20, text=u"\u2193",
                                                command=lambda x=i: self.changeSorting(2*x + 1) )
            downArrowButton.grid(row=0, column=i + 1, pady=10, padx=25, sticky='e')


    @abstractmethod
    def reloadData(self):
        pass

class SortingTable(AbstractSortingTable):



    def buildTable(self):
        super().buildTable()

        for i, record in enumerate(self.data):
            productIdLabel = tk.Label(self.scene.root, text=str(i + 1))
            productIdLabel.grid(row=i + self.scene.freeRowsOnTop, column=0)
            ProductRow(self, record).create(i)



    def reloadData(self):
        self.data = fileOperations.getAllProductsAsLists()
        self.sort()

