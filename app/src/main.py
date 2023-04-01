import init_db as conn
from flask import Flask, request
from services import users as UserService

app = Flask(__name__)


@app.route("/index")
def index():
    service = UserService
    result = service.all()
    return result


@app.route('/create-user', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        db = conn.get_db_connection()
        data = request.get_json()
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
        return 'user saved'

