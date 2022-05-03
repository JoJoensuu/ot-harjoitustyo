class Exercise:
    """Represents single exercise.

    Attributes:
        name: string, exercise name.
        sets: integer for how many sets included.
        reps: integer for how many reps in a single set.
        rest: integer for how many minutes rest between sets.
        comments: string, optional notes.
    """
    def __init__(self, name, sets=None, reps=None, rest=None, comments=None):
        """Constructor

        Args:
            name (string): exercise name
            sets (integer): how many sets included.
            reps (integer): how many reps in a single set.
            rest (integer): how many minutes rest between sets.
            comments (string): optional notes.
        """
        self.name = name
        self.sets = int(sets)
        self.reps = int(reps)
        self.rest = int(rest)
        self.comments = comments
