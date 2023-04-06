from app.src.dbconn import mariadb as conn
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


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
        access_token = create_access_token(identity=user['names'])
        return access_token
    else:
        return 'Unable to verify', 403







