from exercise_day import Day

class User:
    def __init__(self):
        self.calendar = []

    def new_exercise_day(self):
        day = Day()
        self.calendar.append(day)

    def add_exercise(self, day, exercise, sets, reps):
        self.calendar[day].add_exercise(exercise, sets, reps)

    def list_days(self):
        for day in self.calendar:
            print(day)

    def list_exercises(self):
        for day in self.calendar:
            for exercise in day.list_exercises():
                print(exercise)
