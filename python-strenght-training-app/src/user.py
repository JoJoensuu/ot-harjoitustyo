from exercise_day import Day

class User:
    def __init__(self):
        self.calendar = []

    def __str__(self):
        return str(self.calendar[0])

    def new_exercise_day(self):
        day = Day()
        self.calendar.append(day)

    def add_exercise(self, exercise, day):
        self.calendar[day].add_exercise(exercise)