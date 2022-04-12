from exercise_day import Day

class User:
    def __init__(self):
        self.calendar = []

    def __str__(self):
        return self.calendar

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

if __name__ == "__main__":
    kalle = User()
    kalle.new_exercise_day()
    kalle.add_exercise(0, "Bench press", 3, 5)
    kalle.list_exercises()