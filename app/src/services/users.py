from app.src.dbconn import mariadb as conn


def all():
    query = "select * from users;"
    db = conn()
    # This is the way SQLite works. We will use mariadb, but in case of coming back.
    # result = db.execute(query).fetchall()
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def create(data):
    db = conn()
    names = data['names']
    first_name = data['first_name']
    last_name = data['last_name']
    password = data['password']
    insert = f"INSERT INTO users " \
             f"(names, first_name, last_name, password) " \
             f"values " \
             f"('{names}', '{first_name}', '{last_name}', '{password}'); "
    cursor = db.cursor()
    cursor.execute(insert)
    db.commit()
    return 'user saved.'
