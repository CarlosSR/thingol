from .. import init_db as conn


class UsersService:
    def all(self):
        query = "select * from users;"
        db = conn.get_db_connection()
        result = db.execute(query).fetchall()
        return result