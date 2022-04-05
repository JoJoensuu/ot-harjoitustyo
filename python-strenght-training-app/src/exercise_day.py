from datetime import date

class Day:
    def __init__(self):
        self.exercises = []
        self.date = date.today()
    
    def __str__(self):
        return f"{self.exercises[0]}"

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

if __name__ == "__main__":
    paiva = Day()
    paiva.add_exercise("running")
    print(paiva)