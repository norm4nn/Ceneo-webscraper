from abc import ABC, abstractmethod
import tkinter as tk
import tkmacosx as tkmac

import fileOperations


class AbstractRow(ABC):

    def __init__(self, table, data):
        self.table = table
        self.data = data


    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def create(self, rowNumber):
        pass


class ProductRow(AbstractRow):

    def delete(self):
        url = self.data[3]
        fileOperations.deleteUrl(url)
        self.table.scene.rebuild()

    def create(self, rowNumber):

        for i, attribute in enumerate(self.data[:-1]):
            if type(attribute) is float:
                atributeLabel = tk.Label(self.table.scene.root, text="{:.2f}".format(attribute))
            else:
                atributeLabel = tk.Label(self.table.scene.root, text=attribute)
            atributeLabel.grid(row=rowNumber + self.table.scene.freeRowsOnTop, column=i + 1)

        deleteButton = tkmac.Button(self.table.scene.root, bg='red', fg='white', width=30, text='X',
                                    command=self.delete)
        deleteButton.grid(row=rowNumber + self.table.scene.freeRowsOnTop, column=1 + len(self.data), padx=5)