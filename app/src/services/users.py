import init_db as conn


def all():
    query = "select * from users;"
    db = conn.get_db_connection()
    result = db.execute(query).fetchall()
    return result