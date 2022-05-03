from database_connection import get_database_connection

class ExerciseDayRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_day(self, day):
        cursor = self._connection.cursor()
        if not self.check_date_exists(day):
            cursor.execute('INSERT INTO exercise_days (date) VALUES (?)', [day])
            self._connection.commit()
            return True
        else:
            return False

    def list_days(self):
        cursor = self._connection.cursor()
        rows = cursor.execute("select * from exercise_days")
        return rows

    def check_date_exists(self, day):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM exercise_days WHERE date=(?)', [day])
        result = cursor.fetchone()
        return result[1] if result else False

    def get_date_id(self, day):
        cursor = self._connection.cursor()
        cursor.execute('SELECT id FROM exercise_days WHERE date=(?)', [day])
        result = cursor.fetchone()
        return result[0] if result else False

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('delete from exercise_days')
        self._connection.commit()

exercise_day_repository = ExerciseDayRepository(get_database_connection())
