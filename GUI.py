import tkinter as tk
import Scene
import FileService

root = tk.Tk()
root.geometry("800x600")

listScene = Scene.ListScene(root)


def run():
    listScene.rebuild()
    root.mainloop()