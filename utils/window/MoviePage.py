import tkinter as tk


class MoviePage(tk.Frame):
    def __init__(self, parent, controller, movie):
        label = tk.Label(movie.name)
        label.pack
        tk.Frame.__init__(self, parent, bg='#2A2A2A')
