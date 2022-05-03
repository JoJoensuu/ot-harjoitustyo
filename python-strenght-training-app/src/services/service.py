import datetime
from ui.console import Console
from entities.exercise import Exercise
from repositories.exercise_day_repository import ExerciseDayRepository
from database_connection import get_database_connection
from repositories.exercise_repository import ExerciseRepository



class Service:
    def __init__(self):
        self._exercise_days = {}
        self._console = Console()
        self._connection = get_database_connection()
        self._exercise_day_repository = ExerciseDayRepository(self._connection)
        self._exercise_repository = ExerciseRepository(self._connection)

    def ask_date(self):
        self._console.print_out("Select date: ")
        year = self._console.read_year()
        month = self._console.read_month()
        day = self._console.read_day()
        date = datetime.datetime(year, month, day)
        return date

    def list_exercise_days(self):
        days = self._exercise_day_repository.list_days()
        for day in days:
            print(day[0])

    def add_exercise_day(self):
        date = self.ask_date()
        id = self._exercise_day_repository.get_date_id(date)
        if not id:
            self._exercise_day_repository.add_day(date)
        else:
            self._console.print_out("Date already in calendar")

    def add_exercise(self):
        date = self.ask_date()
        if not self._exercise_day_repository.get_date_id(date):
            self._exercise_day_repository.add_day(date)
        date_id = self._exercise_day_repository.get_date_id(date)
        while True:
            self._console.print_out("Enter exercise, 0 to quit, leave empty to skip")
            name = self._console.read_input("Movement name: ")
            if name == "0":
                break
            sets = self._console.read_input("Sets: ")
            reps = self._console.read_input("Reps: ")
            rest = self._console.read_input("Rest between sets (minutes): ")
            comments = self._console.read_input("Exercise notes: ")
            exercise = Exercise(name, sets, reps, rest, comments)
            request = self._exercise_repository.add_exercise(date_id, exercise)
            if not request:
                self._console.print_out("Adding exercise failed")

    def list_exercises_in_day(self):
        date = self.ask_date()
        id = self._exercise_day_repository.get_date_id(date)
        if not id:
            self._console.print_out(f"No exercises for {date}")
        else:
            request = self._exercise_repository.list_exercises(id)
            for row in request:
                self._console.print_out(
                    f"ID: {row[0]} Exercise: {row[1]}, {row[2]} sets, {row[3]} reps"
                )
