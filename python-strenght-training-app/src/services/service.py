import datetime
from ui.console import Console
from repositories.exercise_day_repository import ExerciseDayRepository
from database_connection import get_database_connection
from repositories.exercise_repository import ExerciseRepository



class Service:
    def __init__(self):
        self._exercise_days = {}
        self._console = Console()
        self._connection = get_database_connection()
        self._exerciseDayRepository = ExerciseDayRepository(self._connection)
        self._exerciseRepository = ExerciseRepository(self._connection)

    def ask_date(self):
        self._console.print_out("Select date: ")
        year = self._console.read_year()
        month = self._console.read_month()
        day = self._console.read_day()
        date = datetime.datetime(year, month, day)
        return date

    def list_exercise_days(self):
        days = self._exerciseDayRepository.list_days()
        for day in days:
            print(day[0])

    def add_exercise_day(self):
        date = self.ask_date()
        request = self._exerciseDayRepository.add_day(date)
        if not request:
            self._console.print_out("Date already in calendar")
        else:
            self._console.print_out("Adding date was successful")

    def add_exercise(self):
        date = self.ask_date()
        if not self._exerciseDayRepository.get_date_id(date):
            self._exerciseDayRepository.add_day(date)
        while True:
            self._console.print_out("Enter exercise, 0 to quit")
            name = self._console.read_input("Movement name: ")
            if name == "0":
                break
            sets = self._console.read_input("Sets: ")
            reps = self._console.read_input("Reps: ")
            self._exerciseRepository.add_exercise(date, name, sets, reps)

    def list_exercises_in_day(self):
        date = self.ask_date()
        id = self._exerciseDayRepository.get_date_id(date)
        if not id:
            self._console.print_out(f"No exercises for {date}")
        else:
            request = self._exerciseRepository.list_exercises(id)
            for row in request:
                self._console.print_out(f"ID: {row[0]} Exercise: {row[1]}, {row[2]} sets, {row[3]} reps")
