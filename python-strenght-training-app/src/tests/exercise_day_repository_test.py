import unittest
import datetime
from repositories.exercise_day_repository import ExerciseDayRepository

class TestExerciseDayRepository(unittest.TestCase):
    def setUp(self):
        ExerciseDayRepository.delete_all(self)
        self.date1 = datetime.datetime(2022,5,1)
        self.date2 = datetime.datetime(1990, 12, 1)

    def test_add_day_adds_day_to_database(self):
        ExerciseDayRepository.add_day(self.date1)
        days = ExerciseDayRepository.list_days()
        self.assertEqual(len(days), 1)