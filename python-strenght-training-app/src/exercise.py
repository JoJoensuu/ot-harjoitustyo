class Exercise:
    def __init__(self, name: str, sets: int, reps: int):
        self.name = name
        self.sets = sets
        self.reps = reps

    def __str__(self):
        return f"{self.name}: {self.sets} sets of {self.reps} reps."
