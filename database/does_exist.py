def does_exist(conn, movie_id):
    c = conn.cursor()
    c.execute('SELECT ID FROM Movies WHERE MovieID=?', movie_id)
    data = c.fetchall()
    if data is None:
        return False
    else:
        return True
