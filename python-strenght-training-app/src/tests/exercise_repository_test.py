import unittest
import datetime
from repositories.exercise_repository import exercise_repository
from repositories.exercise_day_repository import exercise_day_repository

class TestExerciseDayRepository(unittest.TestCase):
    def setUp(self):
        exercise_day_repository.delete_all()
        self.date1 = datetime.datetime(2022, 5, 1)
        exercise_day_repository.add_day(self.date1)

    def test_add_exercise_adds_exercise_to_database(self):
        exercise_repository.add_exercise(self.date1, "Test1", "1", "1")
        result = exercise_repository.list_exercises(1)
        list = [row for row in result]
        self.assertEqual(len(list), 1)

    def test_delete_all_removes_exercises_from_day(self):
        exercise_repository.add_exercise(self.date1, "Test1", "1", "1")
        exercise_repository.delete_all(1)
        result = exercise_repository.list_exercises(1)
        list = [row for row in result]
        self.assertEqual(len(list), 0)

    def test_delete_single_removes_one_exercise(self):
        exercise_repository.add_exercise(self.date1, "Test1", "1", "1")
        exercise_repository.add_exercise(self.date1, "Test2", "2", "2")
        exercise_repository.delete_single(2)
        result = exercise_repository.list_exercises(1)
        list = [row for row in result]
        self.assertEqual(len(list), 1)

    def test_get_exercise_data_returns_correct_line(self):
        exercise_repository.add_exercise(self.date1, "Test1", "1", "1")
        exercise_repository.add_exercise(self.date1, "Test2", "2", "2")
        request = exercise_repository.get_exercise_data(1)
        string = request[1]
        self.assertEqual(string, "Test1")