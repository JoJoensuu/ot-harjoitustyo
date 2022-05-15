import unittest
import datetime
from repositories.exercise_day_repository import exercise_day_repository_test

class TestExerciseDayRepository(unittest.TestCase):
    def setUp(self):
        exercise_day_repository_test.delete_all()
        self.date1 = datetime.datetime(2022,5,1)
        self.date2 = datetime.datetime(2022, 12, 10)

    def test_add_day_adds_day_to_database(self):
        exercise_day_repository_test.add_day(self.date1)
        days = exercise_day_repository_test.list_days()
        list = [day for day in days]
        self.assertEqual(len(list), 1)

    def test_list_days_returns_list_False_if_no_dates(self):
        self.assertEqual(exercise_day_repository_test.list_days(), False)

    def test_list_days_returns_list_object_if_dates(self):
        exercise_day_repository_test.add_day(self.date1)
        self.assertEqual(type(exercise_day_repository_test.list_days()), list)

    def test_get_date_id_returns_id(self):
        exercise_day_repository_test.add_day(self.date1)
        self.assertEqual(exercise_day_repository_test.get_date_id(self.date1), 1)

    def test_get_date_id_returns_false_if_not_in_database(self):
        self.assertEqual(exercise_day_repository_test.get_date_id(self.date1), False)

    def test_delete_single_removes_one_day(self):
        exercise_day_repository_test.add_day(self.date1)
        exercise_day_repository_test.add_day(self.date2)
        exercise_day_repository_test.delete_single(1)
        days = exercise_day_repository_test.list_days()
        list = [day for day in days]
        self.assertEqual(len(list), 1)