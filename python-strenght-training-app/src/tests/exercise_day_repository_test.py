import unittest
import datetime
from repositories.exercise_day_repository import exercise_day_repository

class TestExerciseDayRepository(unittest.TestCase):
    def setUp(self):
        exercise_day_repository.delete_all()
        self.date1 = datetime.datetime(2022,5,1)

    def test_add_day_adds_day_to_database(self):
        exercise_day_repository.add_day(self.date1)
        days = exercise_day_repository.list_days()
        list = [day for day in days]
        self.assertEqual(len(list), 1)

    def test_add_day_adding_same_date_returns_false(self):
        exercise_day_repository.add_day(self.date1)
        self.assertEqual(exercise_day_repository.add_day(self.date1), False)

    def test_get_date_id_returns_id(self):
        exercise_day_repository.add_day(self.date1)
        self.assertEqual(exercise_day_repository.get_date_id(self.date1), 1)