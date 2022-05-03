from os import curdir
from database_connection import get_database_connection

class ExerciseRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_exercise(self, day, name, sets, reps):
        cursor = self._connection.cursor()
        cursor.execute('SELECT id FROM exercise_days WHERE date=(?)', [day])
        result = cursor.fetchone()
        day_id = result[0]
        print(day_id)
        cursor.execute('INSERT INTO exercises (day_id, name, sets, reps) VALUES (?, ?, ?, ?)', (day_id, name, sets, reps))
        self._connection.commit()


exercise_repository = ExerciseRepository(get_database_connection())