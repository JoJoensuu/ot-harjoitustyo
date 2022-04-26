import datetime
from ui.console import Console
from entities.exercise import Exercise

class Service:
    def __init__(self):
        self._exercise_days = {}
        self._console = Console()

    def ask_date(self):
        self._console.print_out("Select date: ")
        year = self._console.read_year()
        month = self._console.read_month()
        day = self._console.read_day()
        date = datetime.datetime(year, month, day)
        return date

    def list_exercise_days(self):
        for day in self._exercise_days:
            print(day)

    def add_exercise_day(self):
        date = self.ask_date()
        if date not in self._exercise_days:
            self._exercise_days[date] = []
        else:
            self._console.print_out("Date already in calendar")

    def add_exercise(self):
        date = self.ask_date()
        if date not in self._exercise_days:
            self._exercise_days[date] = []
        while True:
            self._console.print_out("Enter exercise, 0 to quit")
            name = self._console.read_input("Movement name: ")
            if name == "0":
                break
            sets = self._console.read_input("Sets: ")
            reps = self._console.read_input("Reps: ")
            movement = Exercise(name, sets, reps)
            self._exercise_days[date].append(movement)

    def list_exercises_in_day(self):
        date = self.ask_date()
        if date not in self._exercise_days:
            self._console.print_out("Date not in calendar")
            return
        else:
            for exercise in self._exercise_days[date]:
                self._console.print_out(exercise)

