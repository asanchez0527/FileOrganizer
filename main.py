import tkinter as tk
from search import search
import os
from tkinter import filedialog
import database.connect
from database.insert_movie import insert_movie


def main():
    # try to connect to database else create new database
    conn = database.connect.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Movies (MovieID INTEGER, MovieName STRING,'
        'Description STRING, ReleaseDate STRING, Path STRING, Image STRING)'
    )

    # initialize vars
    file_list = []
    video_files = []
    movies = []

    # craft api url
    api_key = 'https://api.themoviedb.org/3/search/movie?api_key=' + input('Enter api key')

    # ask user to select the root folder of all their movies
    path = pick_folder()
    # search root directory and all subdirectories for video files and add them to a list
    for root, dirs, files in os.walk(path, False):
        for name in files:
            file_list.append(os.path.join(root, name))

    # remove all non video files
    for file in file_list:
        if file.endswith('.mkv') or file.endswith('.mp4') or file.endswith('.avi'):
            video_files.append(file)

    # delete file_list variable since we no longer need it
    del file_list

    # search for movie using file name and create a Movie object
    for file in video_files:
        if search(api_key, file) != -1:
            movie = search(api_key, file, conn)
            movies.append(movie)

    # print Movie object
    insert_movie(conn, movies)


# display system dialog for picking folder
def pick_folder():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return path


if __name__ == "__main__":
    main()
