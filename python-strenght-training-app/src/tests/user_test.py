import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_new_user_creates_list(self):
        self.assertEqual(type(self.user.calendar), list)

    def test_new_exercise_day_adds_item_to_calendar(self):
        self.user.new_exercise_day()
        self.assertEqual(len(self.user.calendar), 1)