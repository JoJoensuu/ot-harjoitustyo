import unittest
import datetime
from repositories.exercise_repository import exercise_repository_test
from repositories.exercise_day_repository import exercise_day_repository_test
from entities.exercise import Exercise

class TestExerciseRepository(unittest.TestCase):
    def setUp(self):
        self.date1 = datetime.datetime(2022, 5, 1)
        self.exercise1 = Exercise("Test1", "2", "3", "4", "5")
        self.exercise2 = Exercise("Test2", "12", "13", "14", "15")

    def test_list_exercises_returns_list(self):
        exercise_repository_test.add_exercise(self.date1, self.exercise1)
        result = exercise_repository_test.list_exercises(1)
        for row in result:
            self.assertEqual(row[2], "Test2")

    def test_add_exercise_adds_exercise_to_database(self):
        self.assertEqual(exercise_repository_test.add_exercise(self.date1, self.exercise1), True)

    def test_delete_all_removes_exercises_from_day(self):
        exercise_repository_test.add_exercise(self.date1, self.exercise1)
        self.assertEqual(exercise_repository_test.delete_all(1), True)

    def test_delete_single_removes_one_exercise(self):
        exercise_repository_test.add_exercise(self.date1, self.exercise1)
        exercise_repository_test.add_exercise(self.date1, self.exercise2)
        self.assertEqual(exercise_repository_test.delete_single(2), True)

    def test_get_exercise_data_returns_correct_line(self):
        exercise_repository_test.add_exercise(self.date1, self.exercise1)
        exercise_repository_test.add_exercise(self.date1, self.exercise2)
        request = exercise_repository_test.get_exercise_data(1)
        string = request[2]
        self.assertEqual(string, "Test1")