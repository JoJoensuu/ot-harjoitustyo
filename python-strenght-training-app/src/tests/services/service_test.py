import unittest
from repositories.exercise_day_repository import exercise_day_repository
from repositories.exercise_repository import exercise_repository
from entities.exercise import Exercise
from ui.console import console
from services.service import service

class FakeExerciseRepository:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def list_exercises(self):
        return self.exercises

    def delete_all(self):
        self.exercises = []

    def delete_single(self, exercise_id):
        list = [x for x in self.exercises if x.id != exercise_id]
        self.exercises = list

    def get_exercise_data(self, exercise_id):
        for row in self.exercises:
            if row.id == exercise_id:
                return row

class FakeExerciseDayRepository:
    def __init__(self):
        self.days = []

    def add_day(self, day):
        self.days.append(day)

    def list_days(self):
        return self.days

    def delete_all(self):
        self.days = []

    def delete_single(self, day):
        list = [x for x in self.days if x != day]
        self.days = list

class TestService(unittest.TestCase):
    def setUp(self):
        service.clear_calendar()

    