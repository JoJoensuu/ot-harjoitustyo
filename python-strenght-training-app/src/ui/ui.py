from ui.console import Console
from services.service import Service
import datetime
from initialize_database import initialize_database

COMMANDS = {
    "0": "x QUIT",
    "1": "1 add exercise day",
    "2": "2 add exercise",
    "3": "3 list exercise days",
    "4": "4 list exercises in given day",
    "5": "5 clear calendar",
    "6": "6 remove date from calendar",
    "7": "7 remove all exercises from date",
    "8": "8 remove single exercise",
    "9": "9 list instructions"
}

class UI:
    def __init__(self):
        self._console = Console()
        self._service = Service()

    def start(self):
        initialize_database()
        self._instructions()
        

        while True:
            command = self._console.read_input("command: ")

            if not command in COMMANDS:
                self._console.print_out("false command")

            if command == "0":
                break
            elif command == "1":
                self._add_exercise_day()
            elif command == "2":
                self._add_exercise()
            elif command == "3":
                self._list_exercise_days()
            elif command == "4":
                self._list_exercises_in_day()
            elif command == "5":
                self._clear_calendar()
            elif command == "6":
                self._remove_date()
            elif command == "7":
                self._clear_exercises()
            elif command == "8":
                self._delete_exercise()
            elif command == "9":
                self._instructions()

    def _instructions(self):
        self._console.print_out("Strenght training app")
        for i in COMMANDS:
            self._console.print_out(COMMANDS[i])

    def _ask_date(self):
        self._console.print_out("Select date: ")
        year = self._console.read_year()
        month = self._console.read_month()
        day = self._console.read_day()
        date = datetime.datetime(year, month, day)
        return date

    def _check_date_exists(self):
        date = self._ask_date()
        date_id = self._service.check_date(date)
        if date_id == None:
            return False
        else:
            return date_id

    def _add_exercise_day(self):
        date = self._ask_date()
        if not self._service.add_exercise_day(date):
            self._console.print_out("Adding date failed")

    def _add_exercise(self):
        date = self._ask_date()
        self._service.add_exercise_day(date)
        date_id = self._service.check_date(date)
        while True:
            self._console.print_out("Enter exercise, 0 to quit, leave empty to skip")
            name = self._console.read_input("Movement name: ")
            if name == "0":
                break
            sets = self._console.read_input("Sets: ")
            reps = self._console.read_input("Reps: ")
            rest = self._console.read_input("Rest between sets (minutes): ")
            comments = self._console.read_input("Exercise notes: ")
            if not self._service.add_exercise(date_id, name, sets, reps, rest, comments):
                self._console.print_out("Adding exercise failed")

    def _list_exercise_days(self):
        days = self._service.list_exercise_days()
        if not days:
            self._console.print_out("No dates in calendar")
        else:
            for day in days:
                self._console.print_out(f"Id: {day[0]} - {day[1]}")

    def _list_exercises_in_day(self):
        date_id = self._check_date_exists()
        if not date_id:
            self._console.print_out("Date not in calendar")
        else:
            rows = self._service.list_exercises_in_day(date_id)
            if not rows:
                self._console.print_out("No exercises for selected date")
            else:
                for row in rows:
                    self._console.print_out(f"""ID: {row[0]} Exercise: {row[1]}, {row[2]} sets, {row[3]} reps, {row[4]} minutes rest between sets, notes: {row[5]}""")

    def _clear_calendar(self):
        confirm = self._console.read_input("Confirm clearing calendar with y: ")
        if confirm == "y":
            self._service.clear_calendar()
        else:
            return
    
    def _remove_date(self):
        date_id = self._check_date_exists()
        if not date_id:
            self._console.print_out("Date not in calendar")
        else:
            self._service.remove_date(date_id)

    def _clear_exercises(self):
        date_id = self._check_date_exists()
        if not date_id:
            self._console.print_out("Date not in calendar")
        else:
            self._service.clear_exercises(date_id)
    
    def _delete_exercise(self):
        date_id = self._check_date_exists()
        if not date_id:
            self._console.print_out("Date not in calendar")
        else:
            exercise_id = self._console.read_input("Enter exercise id that you want to remove: ")
            request = self._service.delete_exercise(exercise_id)
            if not request:
                self._console.print_out("Exercise not found")
            else:
                self._console.print_out("Exercise removed")

if __name__ == "__main__":
    app = UI()
    app.start()
