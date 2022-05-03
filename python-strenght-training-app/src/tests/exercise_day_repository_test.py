import unittest
import datetime
from repositories.exercise_day_repository import exercise_day_repository

class TestExerciseDayRepository(unittest.TestCase):
    def setUp(self):
        exercise_day_repository.delete_all()
        self.date1 = datetime.datetime(2022,5,1)
        self.date2 = datetime.datetime(2022, 12, 10)

    def test_add_day_adds_day_to_database(self):
        exercise_day_repository.add_day(self.date1)
        days = exercise_day_repository.list_days()
        list = [day for day in days]
        self.assertEqual(len(list), 1)

    def test_check_date_exists_returns_datetime(self):
        exercise_day_repository.add_day(self.date1)
        self.assertEqual(exercise_day_repository.check_date_exists(self.date1), "2022-05-01 00:00:00")

    def test_check_date_exists_returns_false_if_not_in_database(self):
        self.assertEqual(exercise_day_repository.check_date_exists(self.date1), False)

    def test_add_day_adding_same_date_returns_false(self):
        exercise_day_repository.add_day(self.date1)
        self.assertEqual(exercise_day_repository.add_day(self.date1), False)

    def test_get_date_id_returns_id(self):
        exercise_day_repository.add_day(self.date1)
        self.assertEqual(exercise_day_repository.get_date_id(self.date1), 1)

    def test_delete_single_removes_one_day(self):
        exercise_day_repository.add_day(self.date1)
        exercise_day_repository.add_day(self.date2)
        exercise_day_repository.delete_single(1)
        days = exercise_day_repository.list_days()
        list = [day for day in days]
        self.assertEqual(len(list), 1)