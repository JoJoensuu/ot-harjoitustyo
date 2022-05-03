from database_connection import get_database_connection
from entities.exercise import Exercise

class ExerciseRepository:
    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor()

    def add_exercise(self, date_id, exercise):
        self._cursor.execute(
            'INSERT INTO exercises (day_id, name, sets, reps, rest, comments) VALUES (?, ?, ?, ?, ?, ?)',
             (date_id, exercise.name, exercise.sets, exercise.reps, exercise.rest, exercise.comments)
        )
        self._connection.commit()

    def list_exercises(self, date_id):
        cursor = self._connection.cursor()
        cursor.execute('SELECT id, name, sets, reps, rest, comments FROM exercises WHERE day_id=(?)', [date_id])
        result = cursor.fetchall()
        return result

    def delete_all(self, date_id):
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM exercises WHERE day_id=(?)', [date_id])
        self._connection.commit()

    def delete_single(self, id):
        self._cursor.execute('DELETE FROM exercises WHERE id=(?)', [id])
        self._connection.commit()

    def get_exercise_data(self, id):
        self._cursor.execute('SELECT * FROM exercises WHERE id=(?)', [id])
        result = self._cursor.fetchone()
        return result


exercise_repository = ExerciseRepository(get_database_connection())
