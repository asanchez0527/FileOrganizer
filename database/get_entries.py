def get_entries(conn):
    cursor = conn.cursor()
    return cursor.fetchall()
