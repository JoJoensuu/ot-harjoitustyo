from database_connection import get_database_connection

class ExerciseRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]


user_repository = ExerciseRepository(get_database_connection())
users = user_repository.find_all()