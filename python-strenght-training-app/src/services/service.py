from ui.console import Console
from entities.exercise import Exercise
from repositories.exercise_day_repository import (
    exercise_day_repository as default_exercise_day_repository)
from repositories.exercise_repository import (
    exercise_repository as default_exercise_repository)

class Service:
    """Service entity for communicationg between repositories and the user interface
    """
    def __init__(
        self, exercise_day_repository=default_exercise_day_repository,
        exercise_repository=default_exercise_repository):
        """Class constructor

        Args:
            exercise_day_repository: connects to exercise_day_repository. Defaults to default_exercise_day_repository.
            exercise_repository: connects to exercise_repository. Defaults to default_exercise_repository.
        """
        self._console = Console()
        self._exercise_day_repository = exercise_day_repository
        self._exercise_repository = exercise_repository

    def check_date(self, date):
        """Checks if date exists

        Args:
            date : datetime object

        Returns:
            date_id
        """
        return self._exercise_day_repository.get_date_id(date)

    def check_exercise_exists(self, exercise_id):
        """Checks if exercise exists based on exercise id,
        returns boolean if exists

        Args:
            exercise_id: integer

        Returns:
            Boolean
        """
        if not self._exercise_repository.get_exercise_data(exercise_id):
            return False
        return True

    def add_exercise_day(self, date):
        """Adds new datetime to calendar,
        returns boolean based on success

        Args:
            date : datetime object

        Returns:
            Boolean
        """
        date_id = self._exercise_day_repository.get_date_id(date)
        if not date_id:
            self._exercise_day_repository.add_day(date)
            return True
        return False

    def add_exercise(self, date_id, name, sets, reps, rest, comments):
        """Adds new exercise to exercise_repository

        Args:
            date_id : id for selected date
            name : string
            sets : integer
            reps : integer
            rest : integer
            comments : string
        """
        exercise = Exercise(name, sets, reps, rest, comments)
        self._exercise_repository.add_exercise(date_id, exercise)

    def list_exercise_days(self):
        """Lists exercise days, if any

        Returns:
            List of days or False
        """
        days = self._exercise_day_repository.list_days()
        if not days:
            return False
        return days

    def list_exercises_in_day(self, date_id):
        """Lists exercises in selected date,

        Args:
            date_id

        Returns:
            List of exercises or False
        """
        rows = self._exercise_repository.list_exercises(date_id)
        if not rows:
            return False
        return rows

    def list_all_exercises(self):
        """Lists all exercises in database

        Returns:
            List of exercises or False
        """
        rows = self._exercise_repository.list_all_exercises()
        if not rows:
            return False
        return rows

    def clear_calendar(self):
        """Deletes all exercise days from database
        """
        self._exercise_day_repository.delete_all()

    def remove_date(self, date_id):
        """Remove selected exercise day

        Args:
            date_id
        """
        self._exercise_day_repository.delete_single(date_id)

    def clear_exercises(self):
        """Removes all exercises from database
        """
        self._exercise_repository.delete_all()

    def delete_exercise(self, exercise_id):
        """Delete single exercise from database based on exercise_id

        Args:
            exercise_id

        Returns:
            False if exercise exists, otherwise True
        """
        request = self.check_exercise_exists(exercise_id)
        if not request:
            return False
        self._exercise_repository.delete_single(exercise_id)
        return True

    def check_int(self, value):
        """Checks if given value can be an integer

        Args:
            value: user input

        Returns:
            ValueError if unsuccessful
        """
        try:
            int(value)
            return
        except:
            return ValueError

service = Service()
