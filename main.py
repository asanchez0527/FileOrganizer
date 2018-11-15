import tkinter as tk
from Movie import Movie
import os
from tkinter import filedialog
import requests


def main():
    api_key = 'https://api.themoviedb.org/3/search/movie?api_key=cdf858ef709fd623ee2f4f4befced8aa'
    path = pick_folder()
    list = []
    for root, dirs, files in os.walk(path, False):
        for name in files:
            list.append(os.path.join(root, name))
    video_files = []
    movies = []
    for file in list:
        if file.endswith('.mkv') or file.endswith('.mp4') or file.endswith('.avi'):
            print(file)

    for file in video_files:
        if search(api_key, file[:-4]) != -1:
            movie = search(api_key, file[:-4])
            movies.append(movie)

    for movie in movies:
        print(movie.summary())


def pick_folder():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return path


def search(api_key, name):
    query = api_key + '&query=' + name.replace(" ", "+")
    try:
        response = requests.get(query).json()
        movie_id = response['results'][0]['id']
        name = response['results'][0]['original_title']
        description = response['results'][0]['overview']
        release_date = response['results'][0]['release_date']
        movie = Movie(name, movie_id, description, release_date, os.path.abspath(name))
        return movie
    except IndexError:
        return -1


if __name__ == "__main__":
    main()
