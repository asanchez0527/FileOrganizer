import tkinter as tk
import utils.database.connect
import utils.database.get_entries
import utils.database.Movie


class StartPage(tk.Frame):
    movies = list()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(5)
        self.grid_rowconfigure(1)
        listbox = tk.Listbox(self, bg='red')
        listbox.grid(row=0, column=0)
        self.load_listbox(listbox)

    def load_listbox(self, listbox):
        conn = utils.database.connect.connect('movies.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM movies')
        for row in cursor:
            movie = utils.database.Movie.Movie(movie_id=row[0], name=row[1], description=row[2],
                                               release_date=row[3], path=row[4], image=row[5])
            self.movies.append(movie)
            listbox.insert(tk.END, movie.name)



