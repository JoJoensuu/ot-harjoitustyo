import unittest
from user import User
from exercise_day import Day

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_new_exercise_day_appends_to_calendar(self):
        self.user.new_exercise_day()
        self.assertEqual(len(self.user.calendar), 1)