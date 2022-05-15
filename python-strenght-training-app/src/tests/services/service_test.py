import unittest
from entities.exercise import Exercise
from services.service import Service
from repositories.exercise_day_repository import exercise_day_repository_test
from repositories.exercise_repository import exercise_repository_test
import datetime

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service(exercise_day_repository_test, exercise_repository_test)
        exercise_day_repository_test.delete_all()
        exercise_repository_test.delete_all()
        self.date1 = datetime.datetime(2022, 5, 1)
        self.exercise1 = Exercise("Test1", "2", "3", "4", "5")
        self.exercise2 = Exercise("Test2", "12", "13", "14", "15")

    def test_check_date_returns_date_id(self):
        self.service.add_exercise_day(self.date1)
        self.assertEqual(self.service.check_date(self.date1), 1)

    def test_check_date_returns_none_if_date_not_found(self):
        self.assertEqual(self.service.check_date(self.date1), False)

    def test_check_exercise_exists_success(self):
        self.service.add_exercise(1, "Test1", "2", "3", "4", "Comment")
        self.assertEqual(self.service.check_exercise_exists(1), True)

    def test_check_exercise_exists_fail(self):
        self.assertEqual(self.service.check_exercise_exists(1), False)

    def test_add_exercise_day_success(self):
        self.assertEqual(self.service.add_exercise_day(self.date1), True)

    def test_add_exercise_day_fail(self):
        self.service.add_exercise_day(self.date1)
        self.assertEqual(self.service.add_exercise_day(self.date1), False)

    def test_add_exercise_success(self):
        self.service.add_exercise(1, "Test1", "2", "3", "4", "Comment")
        list = self.service.list_all_exercises()
        self.assertEqual(len(list), 1)

    def test_list_exercise_days_success(self):
        self.service.add_exercise_day(self.date1)
        list = self.service.list_exercise_days()
        self.assertEqual(len(list), 1)

    def test_list_exercise_days_fail(self):
        self.assertEqual(self.service.list_exercise_days(), False)

    def test_list_exercises_in_day_success(self):
        self.service.add_exercise(1, "Test1", "2", "3", "4", "Comment")
        list = self.service.list_exercises_in_day(1)
        self.assertEqual(len(list), 1)

    def test_list_exercises_in_day_fail(self):
        self.assertEqual(self.service.list_exercises_in_day(1), False)

    def test_list_all_exercises_success(self):
        self.service.add_exercise(1, "Test1", "2", "3", "4", "Comment")
        list = self.service.list_all_exercises()
        self.assertEqual(len(list), 1)

    def test_list_all_exercises_fail(self):
        self.assertEqual(self.service.list_all_exercises(), False)

    def test_clear_calendar(self):
        self.service.add_exercise_day(self.date1)
        self.service.clear_calendar()
        self.assertEqual(self.service.list_exercise_days(), False)

    def test_remove_date_success(self):
        self.service.add_exercise_day(self.date1)
        self.service.remove_date(1)
        self.assertEqual(self.service.list_exercise_days(), False)

    def test_remove_date_fail(self):
        self.service.add_exercise_day(self.date1)
        self.service.remove_date(2)
        list = self.service.list_exercise_days()
        self.assertEqual(len(list), 1)

    def test_clear_exercises(self):
        self.service.add_exercise(1, "Test1", "2", "3", "4", "Comment")
        self.service.clear_exercises()
        self.assertEqual(self.service.list_exercises_in_day(1), False)

    def test_delete_exercise_success(self):
        self.service.add_exercise(1, "Test1", "2", "3", "4", "Comment")
        self.service.add_exercise(1, "Test2", "2", "3", "4", "Comment")
        self.service.delete_exercise(1)
        list = [row for row in self.service.list_exercises_in_day(1)]
        exercise = list[0]
        self.assertEqual(exercise[1], "Test2")

    def test_delete_exercise_fail(self):
        self.service.add_exercise(1, "Test1", "2", "3", "4", "Comment")
        self.assertEqual(self.service.delete_exercise(2), False)

    def test_check_int_success(self):
        self.assertNotEqual(self.service.check_int("1"), ValueError)

    def test_check_int_fail(self):
        self.assertEqual(self.service.check_int("tea"), ValueError)