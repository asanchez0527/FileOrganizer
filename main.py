import tkinter as tk
from Movie import Movie
import os
from tkinter import filedialog
import requests


def main():
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


# searches The Movie Database for matches and returns a Movie object
def search(api_key, name):
    query = api_key + '&query=' + name.replace(" ", "+")
    try:
        response = requests.get(query).json()
        movie_id = response['results'][0]['id']
        name = response['results'][0]['original_title']
        description = response['results'][0]['overview']
        release_date = response['results'][0]['release_date']
        movie = Movie(name, movie_id, description, release_date, None)
        return movie
    except IndexError:
        return -1


if __name__ == "__main__":
    main()
