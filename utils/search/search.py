import requests
import re
import os
import datetime
from utils.database.does_exist import does_exist
from utils.search.get_as_base_64 import get_as_base_64


# searches The Movie Database for matches and returns a Movie object
def search(api_key, file, conn):
    # image searching url
    image_url = 'http://image.tmdb.org/t/p/w500'
    # build the query for the api
    name = os.path.basename(file[:-4])

    # init year var
    year = int()

    # try to extract year from name
    for n in name.split():
        temp = str(re.sub(r"\D", "", n))
        if temp.isdigit() and 1890 <= int(temp) <= datetime.datetime.now().year:
            name = name.replace(temp, "")
            year = temp
        elif temp.isdigit() and int(temp) > 11:
            name = name.replace(temp, "")

    # create query
    query = api_key + '&query=' + name.replace(" ", "+")

    # parse movie object from json
    try:
        response = requests.get(query).json()
        movie_id = response['results'][0]['id']
        name = response['results'][0]['original_title']
        description = response['results'][0]['overview']
        release_date = response['results'][0]['release_date']
        image = image_url + response['results'][0]['poster_path']
        path = file
        temp = requests.get(image).content
        image = str()

        # check if movie_posters folder exists, else create folder
        if not os.path.exists('movie_posters'):
            os.mkdir('movie_posters')

        # write image to disk
        with open("movie_posters/" + name + ".jpg", "wb") as f:
            f.write(temp)
            image = "movie_posters/" + name + ".jpg"

        # create movie object
        movie = (movie_id, name, description, release_date, path, image)

    # check if movie exists
        if does_exist(conn, movie_id):
            return 1
        else:
            return movie

    except IndexError:
        print(name)
        return -1
