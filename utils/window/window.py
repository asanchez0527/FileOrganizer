import tkinter as tk
import utils.window.Menu


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.title = 'MovieFlix'
        self.menu = utils.window.Menu.MenuBar(parent)
        parent.config(menu=self.menu)




