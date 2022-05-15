from database_connection import get_database_connection, get_test_database_connection

class ExerciseDayRepository:
    """Repository for handling the exercise_day database
    """
    def __init__(self, connection):
        """

        Args:
            connection: connection entity for database
            cursor: cursor object for database
        """
        self._connection = connection
        self._cursor = self._connection.cursor()

    def add_day(self, day):
        """Inserts date into database

        Args:
            day: datetime object
        """
        self._cursor.execute('INSERT INTO exercise_days (date) VALUES (?)', [day])
        self._connection.commit()

    def list_days(self):
        """Lists dates in database

        Returns:
            List of dates if exist, else returns False
        """
        self._cursor.execute("select * from exercise_days")
        rows = self._cursor.fetchall()
        return rows if rows else False

    def get_date_id(self, day):
        """Gets date_id for selected date

        Args:
            day: datetime object

        Returns:
            date_id for selected date or False if doesn't exist
        """
        self._cursor.execute('SELECT id FROM exercise_days WHERE date=(?)', [day])
        result = self._cursor.fetchone()
        return result[0] if result else False

    def delete_all(self):
        """Deletes dates from database
        """
        self._cursor.execute('delete from exercise_days')
        self._connection.commit()

    def delete_single(self, date_id):
        """Deletes single date

        Args:
            date_id: id for the date
        """
        self._cursor.execute('DELETE FROM exercise_days WHERE id=(?)', [date_id])
        self._connection.commit()


exercise_day_repository = ExerciseDayRepository(get_database_connection())
exercise_day_repository_test = ExerciseDayRepository(get_test_database_connection())
