from console import Console
from service import Service

COMMANDS = {
    "0": "x QUIT",
    "1": "1 add exercise day",
    "2": "2 add exercise",
    "3": "3 list exercises in given day"
}

class UI:
    def __init__(self):
        self._console = Console()
        self._service = Service()

    def start(self):
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

    def _instructions(self):
        self._console.print_out("Strenght training app")
        for command in COMMANDS:
            self._console.print_out(command)

    def _add_exercise_day(self):
        self._service.add_exercise_day()

    def _add_exercise(self):
        self._service.add_exercise()

    def _list_exercises_in_day(self):
        self._service.list_exercises_in_day()

if __name__ == "__main__":
    app = UI()
    app.start()