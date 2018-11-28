def get_entries(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies')
    results = cursor.fetchall()
    return results
