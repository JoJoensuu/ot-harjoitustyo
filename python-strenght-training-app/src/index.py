from user import User
from exercise_day import Day

def main():
    kalle = User()
    kalle.new_exercise_day()
    kalle.add_exercise("running", 0)
    print(kalle)

if __name__ == "__main__":
    main()