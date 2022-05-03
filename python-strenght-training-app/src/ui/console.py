class Console:
    """Reads user inputs and prints output.
    """
    def print_out(self, string):
        """Output text function.

        Args:
            string (string): prints out parameter string.
        """
        print(string)

    def read_input(self, string):
        command = input(string)
        return command

    def read_year(self):
        while True:
            command = input("Enter year (4 digits): ")
            try:
                year = int(command)
            except:
                self.print_out("Non-int data type")
                continue
            if len(command) != 4:
                self.print_out("Year needs to be a four digit input")
            elif year < 2022:
                self.print_out("Cannot enter past years")
            else:
                return year

    def read_month(self):
        while True:
            command = input("Enter month (1-2 digits): ")
            try:
                month = int(command)
            except:
                self.print_out("Non-int data type")
                continue
            if len(command) > 2:
                self.print_out("Month needs to be a 1-2 digit input")
            elif month > 12 or month < 1:
                self.print_out("Enter value between 1-12")
            else:
                return month

    def read_day(self):
        while True:
            command = input("Enter day (1-2 digits): ")
            try:
                day = int(command)
            except:
                self.print_out("Non-int data type")
                continue
            if day > 31 or day < 1:
                self.print_out("Enter value between 1-31")
            else:
                return day

console = Console()