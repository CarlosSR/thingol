from flask import Flask, request, jsonify
from services import users as UserService

app = Flask(__name__)


@app.route("/index")
def index():
    service = UserService
    result = service.all()
    return jsonify(result)


@app.route('/create-user', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
        result = UserService.create(data)
        return result

