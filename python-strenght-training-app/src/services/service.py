from ui.console import Console
from entities.exercise import Exercise
from repositories.exercise_day_repository import (
    exercise_day_repository as default_exercise_day_repository)
from repositories.exercise_repository import (
    exercise_repository as default_exercise_repository)

class Service:
    def __init__(
        self, exercise_day_repository=default_exercise_day_repository,
        exercise_repository=default_exercise_repository):
        self._console = Console()
        self._exercise_day_repository = exercise_day_repository
        self._exercise_repository = exercise_repository

    def check_date(self, date):
        return self._exercise_day_repository.get_date_id(date)

    def check_exercise_exists(self, exercise_id):
        if not self._exercise_repository.get_exercise_data(exercise_id):
            return False
        else:
            return True

    def add_exercise_day(self, date):
        date_id = self._exercise_day_repository.get_date_id(date)
        if not date_id:
            self._exercise_day_repository.add_day(date)
            return True
        return False

    def add_exercise(self, date_id, name, sets, reps, rest, comments):
        exercise = Exercise(name, sets, reps, rest, comments)
        if not self._exercise_repository.add_exercise(date_id, exercise):
            return False
        return True

    def list_exercise_days(self):
        days = self._exercise_day_repository.list_days()
        if days == None:
            return False
        return days

    def list_exercises_in_day(self, date_id):
        rows = self._exercise_repository.list_exercises(date_id)
        if rows == None:
            return False
        return rows

    def clear_calendar(self):
        self._exercise_day_repository.delete_all()

    def remove_date(self, date_id):
        self._exercise_day_repository.delete_single(date_id)

    def clear_exercises(self, date_id):
        date_id = self.check_date()
        if not date_id:
            self._console.print_out("Date not in calendar")
        else:
            self._exercise_repository.delete_all(date_id)

    def delete_exercise(self, exercise_id):
        request = self.check_exercise_exists(exercise_id)
        if not request:
            return False
        else:
            self._exercise_repository.delete_single(exercise_id)
            return True
