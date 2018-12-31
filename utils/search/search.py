import requests
import os
from utils.database.does_exist import does_exist
from utils.search.get_as_base_64 import get_as_base_64


# searches The Movie Database for matches and returns a Movie object
def search(api_key, file, conn):
    # image searching url
    image_url = 'http://image.tmdb.org/t/p/w500'
    # build the query for the api
    name = os.path.basename(file[:-4])
    query = api_key + '&query=' + name.replace(" ", "+")
    try:
        response = requests.get(query).json()
        movie_id = response['results'][0]['id']
        name = response['results'][0]['original_title']
        description = response['results'][0]['overview']
        release_date = response['results'][0]['release_date']
        image = image_url + response['results'][0]['poster_path']
        path = file
        movie = (movie_id, name, description, release_date, path, get_as_base_64(image))
        temp = requests.get(image).content
        with open("resources/" + name + ".jpg", "wb") as f:
            f.write(temp)
        if does_exist(conn, movie_id):
            return 1
        else:
            return movie
    except IndexError:
        print(name)
        return -1
