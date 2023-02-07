import tkinter as tk
import tkmacosx as tkmac

import fileOperations
import SceneElement




class ProductInput(SceneElement.AbstractSceneElement):

    def create(self):
        urlInput = tk.Entry(self.scene.root)
        addButton = tkmac.Button(self.scene.root, bg='green', fg='white', text='Add url',
                                 command=lambda: self.addRecord(urlInput.get()))
        urlInput.grid(row=self.scene.getInputRow(), column=1, pady=20)
        urlInput.focus()
        addButton.grid(row=self.scene.getInputRow(), column=2)

    def addRecord(self, url):
        fileOperations.addUrl(url)
        self.scene.rebuild()