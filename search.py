import requests
from Movie import Movie


# searches The Movie Database for matches and returns a Movie object
def search(api_key, name):
    # image searching url
    image_url = 'http://image.tmdb.org/t/p/w500'
    # build the query for the api
    query = api_key + '&query=' + name.replace(" ", "+")
    try:
        response = requests.get(query).json()
        movie_id = response['results'][0]['id']
        name = response['results'][0]['original_title']
        description = response['results'][0]['overview']
        release_date = response['results'][0]['release_date']
        image = image_url + response['results'][0]['poster_path']
        movie = Movie(name, movie_id, description, release_date, None, image)
        return movie
    except IndexError:
        return -1
