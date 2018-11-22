from sqlite3 import Error


def does_exist(conn, movie_id):
    c = conn.cursor()
    try:
        c.execute('SELECT MovieID FROM Movies WHERE MovieID=?', (movie_id,))
        data = c.fetchall()
        if not data:
            return False
        else:
            return True
    except Error as e:
        print(e)
        return False
