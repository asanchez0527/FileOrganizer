import tkinter as tk
import utils.database.connect
from utils.database.get_entries import get_entries
from PIL import Image, ImageTk
import base64
import glob
import os
from utils.window.MoviePage import MoviePage


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#2B2B2B')

        listbox = tk.Listbox(self, bg='#1c1c1c', fg="white")
        self.grid_columnconfigure(0)
        for i in range(4):
            self.grid_columnconfigure(i+1, weight=1, minsize=150)
            self.grid_rowconfigure(i, weight=1, minsize=200)

        listbox.grid(column=0, sticky=tk.NSEW, rowspan=4)
        self.load_listbox(listbox)

        COLUMNS = 4
        image_count = 0

        for image in glob.glob('resources/*.jpg'):
            image_count += 1
            r, c = divmod(image_count-1, COLUMNS)
            im = Image.open(image)
            resized = im.resize((100, 150), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized)
            myvar = tk.Button(self, image=tkimage, text=os.path.basename(image)[:-4], command=lambda: self.popupmsg())
            myvar.image = tkimage
            myvar.config()
            myvar.grid(row=r, column=c+1, padx=10, pady=10)


        # label = tk.Label(self, text=listbox.curselection())
        # label.grid(column=1)


    def load_listbox(self, listbox):
        conn = utils.database.connect.connect('movies.db')
        movies = get_entries(conn)
        for movie in movies:
            listbox.insert(tk.END, movie.name)

    def popupmsg(self, msg):
        popup = tk.Tk()
        popup.wm_title()
        label = tk.Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy, fg="black")
        B1.pack()
        popup.mainloop()
