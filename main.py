import tkinter as tk
from search import search
import os
from tkinter import filedialog
import database.connect
from sqlite3 import Error



def main():
    # try to connect to database else create new database
    try:
        conn = database.connect.connect_database('movies.db')
    except IOError:
        print('Could not find db file... creating new...')

    cursor = conn.cursor()


    # initialize vars
    file_list = []
    video_files = []
    movies = []

    # craft api url
    api_key = 'https://api.themoviedb.org/3/search/movie?api_key=' + input('Enter your api key: ')

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
        if search(api_key, os.path.basename(file[:-4])) != -1:
            movie = search(api_key, os.path.basename(file[:-4]))
            movie.path = file
            movies.append(movie)

    # print Movie object
    for movie in movies:
        print(movie.summary())


# display system dialog for picking folder
def pick_folder():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return path


if __name__ == "__main__":
    main()
