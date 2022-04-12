import unittest
from exercise_day import Day

class TestUser(unittest.TestCase):
    def setUp(self):
        self.day = Day()

    def test_new_day_creates_calendar(self):
        self.assertEqual(len(self.day.exercises), 0)

    def test_add_exercise_adds_to_calendar(self):
        self.day.add_exercise("bench press", 1, 1)
        self.assertEqual(len(self.day.exercises), 1)

    def test_list_exercises_returns_list(self):
        self.day.add_exercise("bench press", 1, 1)
        self.assertEqual(type(self.day.list_exercises()), list)