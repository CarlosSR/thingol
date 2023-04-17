from flask import Flask, request, jsonify
from app.src.dbconn import mariadb as db_connection
from services import users as UserService
from services.RolesService import RolesService
from services.EnrollmentService import EnrollmentService
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)
db = db_connection()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = UserService.login(data)
    return jsonify({"token": result})

#Endpoints generales
# @app.route('/list/<role>/<status>', methods=['GET'])  # lista de filtrados usuarios por rol y status
@app.route("/users/all")  # list of active users.
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


@app.route('/roles')  # GET, list of roles
@jwt_required()
def roles_list():
    service = RolesService(db).query_roles()
    return jsonify(service)


@app.route('/assign-role', methods=['POST'])  # assign role
@jwt_required()
def assign_role():
    data = request.get_json()
    service = RolesService(db)
    result = service.assign_role(data)
    return jsonify(result)

# Solicitud de tutor para acceso a sistema.



#Inscripcion
@app.route('/enroll/partial/<phase>', methods=['POST'])  # registro de alumnos a un grado. Status inactivo. tutores registran
def partial_enroll():
    data = request.get_json()
    result = EnrollmentService(db).partial_register(data)
    return jsonify(result)

# @app.route('/enroll/complete', methods=['POST']  # cambio de status de alumno inscrito.

# @app.route('/class', methods=['POST'])  # un administrativo crea un grupo para que los alumnos se puedan inscribir
