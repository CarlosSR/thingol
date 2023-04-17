from mysql.connector import Error


class EnrollmentService:
    def __init__(self, conn):
        self.db = conn

    def partial_register(self, data):

        # registro en users, asignación de rol y en enrollments
        names = data['names']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        hashed_pass = 'temporal_hash'
        insert_user = f'''INSERT INTO users 
                          (names, first_name, last_name, email, password, status) 
                          values
                          ('{names}', '{first_name}', '{last_name}', '{email}', '{hashed_pass}', 0);'''

        try:
            cursor = self.db.cursor()
            cursor.execute(insert_user)
            self.db.commit()
            message = True
        except Error as e:
            message = e

        assign_role = f'''
                        INSERT INTO user_role
                        (user_id, role_id) values ({user_id},{role_id})
                      '''

