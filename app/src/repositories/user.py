from app.src.dbconn import mariadb as conn
from mysql.connector import Error


def all_users():
    db = conn()
    query = "select * from users;"
    cursor = db.cursor(dictionary=True)
    cursor.execute(query)
    return cursor.fetchall()


def create(names, first_name, last_name, email, hashed_pass):
    try:
        db = conn()
        insert = f'''INSERT INTO users 
                       (names, first_name, last_name, email, password) 
                   values
                       ('{names}', '{first_name}', '{last_name}', '{email}', '{hashed_pass}');'''
        cursor = db.cursor()
        cursor.execute(insert)
        db.commit()
        return True
    except Error as e:
        return e
