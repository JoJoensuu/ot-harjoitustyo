import datetime
from ui.console import Console
from entities.exercise import Exercise
from repositories.exercise_day_repository import ExerciseDayRepository
from database_connection import get_database_connection
from initialize_database import initialize_database



class Service:
    def __init__(self):
        self._exercise_days = {}
        self._console = Console()
        self._connection = get_database_connection()
        self._repository = ExerciseDayRepository(self._connection)

    def ask_date(self):
        self._console.print_out("Select date: ")
        year = self._console.read_year()
        month = self._console.read_month()
        day = self._console.read_day()
        date = datetime.datetime(year, month, day)
        return date

    def list_exercise_days(self):
        days = self._repository.find_all()
        for day in days:
            print(day[1])

    def add_exercise_day(self):
        date = self.ask_date()
        self._repository.add_day(date)

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

