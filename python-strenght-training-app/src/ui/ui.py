from ui.console import Console
from services.service import Service
from initialize_database import initialize_database

COMMANDS = {
    "0": "x QUIT",
    "1": "1 add exercise day",
    "2": "2 add exercise",
    "3": "3 list exercises in given day",
    "4": "4 list exercise days",
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
                self._list_exercises_in_day()
            elif command == "4":
                self._list_exercise_days()
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

    def _add_exercise_day(self):
        date = self._service.ask_date()
        self._service.add_exercise_day(date)

    def _add_exercise(self):
        date = self._service.ask_date()
        self._service.add_exercise(date)

    def _list_exercises_in_day(self):
        self._service.list_exercises_in_day()

    def _list_exercise_days(self):
        self._service.list_exercise_days()
    def _clear_calendar(self):
        self._service.clear_calendar()
    
    def _remove_date(self):
        self._service.remove_date()

    def _clear_exercises(self):
        self._service.clear_exercises()
    
    def _delete_exercise(self):
        self._service.delete_exercise()

if __name__ == "__main__":
    app = UI()
    app.start()
