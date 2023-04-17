from mysql.connector import Error
from app.src.utilities import Validator


class RolesService:
    def __init__(self, conn):
        self.db = conn

    def query_roles(self):
        query = "select * from roles;"
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()

    def assign_role(self, data):
        # Just mind to validate the user doesn't have the same role.
        try:
            user_id = data['user_id']
            role_id = data['role_id']
            query = f"INSERT INTO user_role (user_id, role_id) values ({user_id},{role_id})"
            cursor = self.db.cursor()
            cursor.execute(query)
            self.db.commit()
            return True
        except Error as e:
            return e

    def validate_user_roles(self):
        pass