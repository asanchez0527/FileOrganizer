import sqlite3


def insert_movie(conn, movie):
    try:
        sql = 'INSERT INTO Movies (MovieID, MovieName, Description, ReleaseDate, Path, Image) VALUES (?, ?, ?, ?, ?, ?)'
        c = conn.cursor()
        c.executemany(sql, movie)
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0])
    conn.commit()
