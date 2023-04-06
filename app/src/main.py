from flask import Flask, request, jsonify, session, flash
from services import users as UserService
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = UserService.login(data)
    return jsonify(result)


@app.route("/index")
@jwt_required()
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

