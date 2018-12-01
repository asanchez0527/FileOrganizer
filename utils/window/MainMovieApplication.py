import tkinter as tk
from utils.window.StartPage import StartPage
from utils.window.Menu import MenuBar
from utils.window.SettingsPage import SettingsPage


class MainMovieApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.minsize(500,400)

        self.frames = {}

        for F in (StartPage, SettingsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        menu = MenuBar(container, self)
        self.config(menu=menu)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()




