class Exercise:
    def __init__(self, name, sets=None, reps=None):
        self.name = name
        self.sets = sets
        self.reps = reps

    def __str__(self):
        return f"Exercise: {self.name}, sets: {self.sets}, reps: {self.reps}"