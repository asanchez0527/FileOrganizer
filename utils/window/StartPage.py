import tkinter as tk
import utils.window.Menu


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Start page', font=('Verdana', 10))
        label.pack(pady=10, padx=10)
