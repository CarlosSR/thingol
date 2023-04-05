from app.src.dbconn import mariadb as conn
from app.src.main import app as app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from flask import make_response


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
    email = data['email']
    hashed_pass = generate_password_hash(password)
    insert = f'''INSERT INTO users 
                    (names, first_name, last_name, email, password) 
                values
                    ('{names}', '{first_name}', '{last_name}', '{email}', '{hashed_pass}');'''
    cursor = db.cursor()
    cursor.execute(insert)
    db.commit()
    return 'user saved.'


def login(data):
    db = conn()
    email = data['email']
    password = data['password']
    query = f"SELECT * FROM users WHERE email = '{email}'"
    cursor = db.cursor(dictionary=True)
    cursor.execute(query)
    user = cursor.fetchone()
    if check_password_hash(user['password'], password):
        token = jwt.encode({
            'user': user.get('first_name'),
            'exp': str(datetime.utcnow() + timedelta(seconds=1800)),
        }, '1234567890')
        return {'token': token}
    else:
        return 'Unable to verify', 403







