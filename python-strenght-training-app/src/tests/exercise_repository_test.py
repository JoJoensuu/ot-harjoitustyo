import unittest
import datetime
from repositories.exercise_repository import exercise_repository_test
from entities.exercise import Exercise

class TestExerciseRepository(unittest.TestCase):
    def setUp(self):
        exercise_repository_test.delete_all()
        self.exercise1 = Exercise("Test1", "2", "3", "4", "5")
        self.exercise2 = Exercise("Test2", "12", "13", "14", "15")

    def test_add_exercise_success(self):
        exercise_repository_test.add_exercise(1, self.exercise1)
        list = [row for row in exercise_repository_test.list_exercises(1)]
        self.assertEqual(len(list), 1)
        
    def test_list_exercises_returns_list_if_exercises(self):
        exercise_repository_test.add_exercise(1, self.exercise1)
        exercise_repository_test.add_exercise(1, self.exercise2)
        list = [row for row in exercise_repository_test.list_exercises(1)]
        self.assertEqual(len(list), 2)

    def test_list_exercises_returns_false(self):
        self.assertEqual(exercise_repository_test.list_exercises(1), False)

    def test_delete_all_removes_exercises(self):
        exercise_repository_test.add_exercise(1, self.exercise1)
        exercise_repository_test.delete_all()
        self.assertEqual(exercise_repository_test.list_exercises(1), False)

    def test_delete_single_removes_one_exercise(self):
        exercise_repository_test.add_exercise(1, self.exercise1)
        exercise_repository_test.add_exercise(1, self.exercise2)
        exercise_repository_test.delete_single(2)
        list = [row for row in exercise_repository_test.list_exercises(1)]
        self.assertEqual(len(list), 1)

    def test_get_exercise_data_returns_correct_line(self):
        exercise_repository_test.add_exercise(1, self.exercise1)
        exercise_repository_test.add_exercise(1, self.exercise2)
        request = exercise_repository_test.get_exercise_data(1)
        self.assertEqual(request[2], "Test1")

    def test_list_all_exercises_success(self):
        exercise_repository_test.add_exercise(1, self.exercise1)
        exercise_repository_test.add_exercise(2, self.exercise2)
        list = [row for row in exercise_repository_test.list_all_exercises()]
        self.assertEqual(len(list), 2)

    def test_list_all_exercises_false(self):
        self.assertEqual(exercise_repository_test.list_all_exercises(), False)
