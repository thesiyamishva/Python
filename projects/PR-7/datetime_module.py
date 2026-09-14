from datetime import datetime
import time


def display_current_datetime():
    now = datetime.now()

    print("\nCurrent Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))


def date_difference():
    try:
        date1 = input("\nEnter the first date (YYYY-MM-DD): ")
        date2 = input("Enter the second date (YYYY-MM-DD): ")

        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        difference = abs((d2 - d1).days)

        print("Difference:", difference, "days")

    except ValueError:
        print("Invalid date format.")


def custom_date_format():
    try:
        date_input = input("\nEnter date (YYYY-MM-DD): ")

        date = datetime.strptime(date_input, "%Y-%m-%d")

        print("Formatted Date:", date.strftime("%d-%m-%Y"))
        print("Day:", date.strftime("%A"))
        print("Month:", date.strftime("%B"))
        print("Year:", date.strftime("%Y"))

    except ValueError:
        print("Invalid date format.")


def stopwatch():
    input("\nPress Enter to start the stopwatch...")

    start = time.time()

    input("Press Enter to stop the stopwatch...")

    end = time.time()

    elapsed = end - start

    print("Elapsed Time:", round(elapsed, 2), "seconds")


def countdown_timer():
    try:
        seconds = int(input("\nEnter countdown time in seconds: "))

        if seconds <= 0:
            print("Enter a number greater than zero.")
            return

        while seconds > 0:
            print("Time remaining:", seconds, "seconds")

            time.sleep(1)

            seconds -= 1

        print("Time's up!")

    except ValueError:
        print("Please enter a valid number.")


def datetime_menu():
    while True:
        print("\n==========================")
        print("Datetime and Time Operations:")
        print("==========================")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_current_datetime()

        elif choice == "2":
            date_difference()

        elif choice == "3":
            custom_date_format()

        elif choice == "4":
            stopwatch()

        elif choice == "5":
            countdown_timer()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    datetime_menu()