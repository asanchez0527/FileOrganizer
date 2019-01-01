from utils.object_model.movie import Movie


def get_entries(conn):
    results = []
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies')
    for row in cursor:
        results.append(Movie(movie_id=row[0], name=row[1], description=row[2],
                             release_date=row[3], path=row[4], image=row[5]))
    return results
