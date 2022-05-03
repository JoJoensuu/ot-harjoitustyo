from database_connection import get_database_connection

class ExerciseDayRepository:
    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor()

    def add_day(self, day):
        self._cursor.execute('INSERT INTO exercise_days (date) VALUES (?)', [day])
        self._connection.commit()

    def list_days(self):
        rows = self._cursor.execute("select * from exercise_days")
        return rows

    def get_date_id(self, day):
        self._cursor.execute('SELECT id FROM exercise_days WHERE date=(?)', [day])
        result = self._cursor.fetchone()
        return result[0] if result else False

    def delete_all(self):
        self._cursor.execute('delete from exercise_days')
        self._connection.commit()

    def delete_single(self, id):
        self._cursor.execute('DELETE FROM exercise_days WHERE id=(?)', [id])
        self._connection.commit()


exercise_day_repository = ExerciseDayRepository(get_database_connection())
