from database_connection import get_database_connection

class ExerciseDayRepository:
    def __init__(self, connection):
        self._connection = get_database_connection()

    def add_day(self, day):
        cursor = self._connection.cursor()

        cursor.execute('INSERT INTO exercise_days (date) VALUES (?)', [day])
        self._connection.commit()
        return day

    def find_all(self):
        cursor = self._connection.cursor()

        rows = cursor.execute("select * from exercise_days")

        

        return rows

exercise_day_repository = ExerciseDayRepository(get_database_connection)
