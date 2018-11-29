import tkinter as tk
import utils.database.connect
from utils.database.get_entries import get_entries
from utils.database.Movie import Movie


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#2B2B2B')
        listbox = tk.Listbox(self, bg='red')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)
        listbox.grid(column=0, sticky=tk.NS)
        self.load_listbox(listbox)
        # label = tk.Label(self, text=listbox.curselection())
        # label.grid(column=1)

    def load_listbox(self, listbox):
        conn = utils.database.connect.connect('movies.db')
        movies = get_entries(conn)
        for movie in movies:
            listbox.insert(tk.END, movie.name)
