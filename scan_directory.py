import tkinter as tk
from search import search
import os
import database.connect
from database.insert_movie import insert_movie
from pick_folder import pick_folder


def scan_directory(root):
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
    key = 'cdf858ef709fd623ee2f4f4befced8aa'
    api_key = 'https://api.themoviedb.org/3/search/movie?api_key=' + key

    # ask user to select the root folder of all their movies
    path = pick_folder(root)

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
        result = search(api_key, file, conn)
        if result == -1:
            print('Index error')
        elif result == 1:
            print('Movie exists')
        else:
            movies.append(result)

    # print Movie object
    insert_movie(conn, movies)
