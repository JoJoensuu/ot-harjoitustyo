from user import User

def main():
    kalle = User()
    kalle.new_exercise_day()
    kalle.add_exercise(0, "bench press", 5, 5)
    kalle.add_exercise(0, "back squat", 2, 6)
    kalle.list_exercises()

if __name__ == "__main__":
    main()