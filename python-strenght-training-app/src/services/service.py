import datetime
from ui.console import Console
from entities.exercise import Exercise
from repositories.exercise_day_repository import (exercise_day_repository as default_exercise_day_repository)
from repositories.exercise_repository import (exercise_repository as default_exercise_repository)

class Service:
    def __init__(self, exercise_day_repository=default_exercise_day_repository, exercise_repository=default_exercise_repository):
        self._console = Console()
        self._exercise_day_repository = exercise_day_repository
        self._exercise_repository = exercise_repository

    def check_date(self):
        date = self.ask_date()
        return self._exercise_day_repository.get_date_id(date)

    def ask_date(self):
        self._console.print_out("Select date: ")
        year = self._console.read_year()
        month = self._console.read_month()
        day = self._console.read_day()
        date = datetime.datetime(year, month, day)
        return date

    def list_exercise_days(self):
        days = self._exercise_day_repository.list_days()
        if days == None:
            self._console.print_out("No dates in calendar")
        else:
            for day in days:
                self._console.print_out(f"Id: {day[0]} - {day[1]}")

    def add_exercise_day(self, date):
        id = self._exercise_day_repository.get_date_id(date)
        if not id:
            self._exercise_day_repository.add_day(date)
        else:
            self._console.print_out("Date already in calendar")

    def add_exercise(self, date):
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
        id = self.check_date()
        if not id:
            self._console.print_out(f"No exercises for selected date")
        else:
            request = self._exercise_repository.list_exercises(id)
            for row in request:
                self._console.print_out(
                    f"ID: {row[0]} Exercise: {row[1]}, {row[2]} sets, {row[3]} reps"
                )

    def clear_calendar(self):
        confirm = self._console.read_input("Confirm clearing calendar with y")
        if confirm != "y":
            return
        else:
            self._exercise_day_repository.delete_all()

    def remove_date(self):
        id = self.check_date()
        if not id:
            self._console.print_out("Date not in calendar")
        else:
            self._exercise_day_repository.delete_single(id)

    def clear_exercises(self):
        id = self.check_date()
        if not id:
            self._console.print_out("Date not in calendar")
        else:
            self._exercise_repository.delete_all(id)

    def delete_exercise(self):
        id = self.check_date()
        if not id:
            self._console.print_out("Date not in calendar")
        else:
            self._exercise_repository.delete_single(id)

