from os import curdir
from database_connection import get_database_connection

class ExerciseRepository:
    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor()

    def add_exercise(self, day, name, sets, reps):
        # needs cleaning up, get id from outside the method if possible
        self._cursor.execute('SELECT id FROM exercise_days WHERE date=(?)', [day])
        result = self._cursor.fetchone()
        day_id = result[0]
        self._cursor.execute('INSERT INTO exercises (day_id, name, sets, reps) VALUES (?, ?, ?, ?)', (day_id, name, sets, reps))
        self._connection.commit()

    def list_exercises(self, id):
        cursor = self._connection.cursor()
        cursor.execute('SELECT id, name, sets, reps FROM exercises WHERE day_id=(?)', [id])
        result = cursor.fetchall()
        return result

    def delete_all(self, id):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM exercises WHERE day_id=(?)', [id])
        self._connection.commit()

    def delete_single(self, id):
        self._cursor.execute('DELETE FROM exercises WHERE id=(?)', [id])
        self._connection.commit()


exercise_repository = ExerciseRepository(get_database_connection())