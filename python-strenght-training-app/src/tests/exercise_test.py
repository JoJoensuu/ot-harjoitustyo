import unittest
from entities.exercise import Exercise

class TestExercise(unittest.TestCase):
    def setUp(self):
        self.example = Exercise("bench press", 2, 5)

    def test_print_exercise(self):
        outcome = str(self.example)
        self.assertEqual(outcome, "bench press: 2 sets of 5 reps.")