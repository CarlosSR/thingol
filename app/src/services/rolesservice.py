from app.src.dbconn import mariadb as conn
from mysql.connector import Error


def query_roles():
    db = conn()
    query = "select * from roles;"
    cursor = db.cursor(dictionary=True)
    cursor.execute(query)
    return cursor.fetchall()


def assign_role(data):
    # Just mind to validate the user doesn't have the same role.
    try:
        db = conn()
        user_id = data['user_id']
        role_id = data['role_id']
        query = f"INSERT INTO user_role (user_id, role_id) values ({user_id},{role_id})"
        cursor = db.cursor(query)
        cursor.execute(query)
        db.commit()
        return True
    except Error as e:
        return e




