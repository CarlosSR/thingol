from app.src.dbconn import mariadb as conn
from mysql.connector import Error
from werkzeug.security import generate_password_hash


def all_users():
    db = conn()
    query = "select * from users;"
    cursor = db.cursor(dictionary=True)
    cursor.execute(query)
    return cursor.fetchall()


def create(response):
    names = response['names']
    first_name = response['first_name']
    last_name = response['last_name']
    email = response['email']
    hashed_pass = generate_password_hash(response['password'])
    try:
        db = conn()
        insert = f'''INSERT INTO users 
                       (names, first_name, last_name, email, password, status) 
                   values
                       ('{names}', '{first_name}', '{last_name}', '{email}', '{hashed_pass}', 1);'''
        cursor = db.cursor()
        cursor.execute(insert)
        db.commit()
        return True
    except Error as e:
        return e
