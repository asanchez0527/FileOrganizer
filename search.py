import requests
from Movie import Movie


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
