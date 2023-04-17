from app.src.dbconn import mariadb as conn
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.src.repositories import user
from app.src.utilities.Validator import Validator


def all():
    users = user.all_users()
    return users


def create(data):
    rules = {
        'names': 'string|required|max:7',
        'first_name': 'string|required|max:7',
        'last_name': 'string|required',
        'password': 'string|required|min:10',
        'email': 'string||min:10'
    }
    validator = Validator(data, rules)
    validator.apply()
    if validator.errors:
        return validator.errors

    return validator.payload
    result = user.create(validator.payload)
    if result:
        return 'User saved.'

    return result


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







