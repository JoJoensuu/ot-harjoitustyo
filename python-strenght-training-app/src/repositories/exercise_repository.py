from database_connection import get_database_connection, get_test_database_connection

class ExerciseRepository:
    """Handles insertions into and deletions from exercise database
    """
    def __init__(self, connection):
        """Class constructor, creates new exercise repository

        Args:
            connection: connection entity for database
            cursor: cursor object for database
        """
        self._connection = connection
        self._cursor = self._connection.cursor()

    def add_exercise(self, date_id, exercise):
        """Inserts exercise into exercise database
        """
        self._cursor.execute(
                """
                INSERT INTO exercises
                (day_id, name, sets, reps, rest, comments)
                VALUES (?, ?, ?, ?, ?, ?)"""
                ,
                (
                    date_id,
                    exercise.name,
                    exercise.sets,
                    exercise.reps,
                    exercise.rest,
                    exercise.comments
                    )
            )
        self._connection.commit()

    def list_exercises(self, date_id):
        """Lists exercises for selected date_id if any,
        otherwise returns False
        """
        self._cursor.execute("""
            SELECT id, name, sets, reps, rest, comments
            FROM exercises where day_id=(?)""", [date_id])
        rows = self._cursor.fetchall()
        return rows if rows else False

    def list_all_exercises(self):
        """Lists exercises in database if any,
        otherwise returns False
        """
        self._cursor.execute("""SELECT id, name, sets, reps, rest, comments FROM exercises""")
        rows = self._cursor.fetchall()
        return rows if rows else False

    def delete_all(self):
        """Deletes all exercies in database
        """
        self._cursor.execute("""
            DELETE FROM exercises
            """)
        self._connection.commit()

    def delete_single(self, exercise_id):
        """Deletes single exercise
        """
        self._cursor.execute("""
            DELETE FROM exercises WHERE id=(?)
            """, [exercise_id])
        self._connection.commit()

    def get_exercise_data(self, exercise_id):
        """Returns exercise data based on exercise_id if any,
        otherwise returns False
        """
        self._cursor.execute("""
        SELECT * FROM exercises WHERE id=(?)
        """, [exercise_id])
        result = self._cursor.fetchone()
        return result if result else False


exercise_repository = ExerciseRepository(get_database_connection())
exercise_repository_test = ExerciseRepository(get_test_database_connection())
