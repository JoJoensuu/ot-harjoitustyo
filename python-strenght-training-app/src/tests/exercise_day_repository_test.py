import unittest
import datetime
from repositories.exercise_day_repository import exercise_day_repository

class TestExerciseDayRepository(unittest.TestCase):
    def setUp(self):
        exercise_day_repository.delete_all()
        self.date1 = datetime.datetime(2022,5,1)
        self.date2 = datetime.datetime(1990, 12, 1)

    def test_add_day_adds_day_to_database(self):
        exercise_day_repository.add_day(self.date1)
        days = exercise_day_repository.list_days()
        list = [day for day in days]
        self.assertEqual(len(list), 1)

    def test_adding_same_date_not_possible(self):
        exercise_day_repository.add_day(self.date1)
        exercise_day_repository.add_day(self.date1)
        days = exercise_day_repository.list_days()
        list = [day for day in days]
        self.assertEqual(len(list), 1)