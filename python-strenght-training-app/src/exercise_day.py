from datetime import date
from exercise import Exercise

class Day:
    def __init__(self):
        self.exercises = []
        self.date = date.today()

    def list_exercises(self):
        return self.exercises

    def add_exercise(self, name, sets, reps):
        exercise = Exercise(name, sets, reps)
        self.exercises.append(exercise)
