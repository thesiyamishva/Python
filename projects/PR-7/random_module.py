import random
import string


def random_number():
    try:
        start = int(input("\nEnter starting number: "))
        end = int(input("Enter ending number: "))

        if start > end:
            print("Starting number must be smaller than ending number.")
        else:
            print("Random Number:", random.randint(start, end))

    except ValueError:
        print("Please enter valid numbers.")


def random_list():
    try:
        size = int(input("\nEnter list size: "))

        if size <= 0:
            print("Size must be greater than zero.")
            return

        numbers = [random.randint(1, 100) for _ in range(size)]

        print("Random List:", numbers)

    except ValueError:
        print("Please enter a valid number.")


def random_password():
    try:
        length = int(input("\nEnter password length: "))

        if length <= 0:
            print("Length must be greater than zero.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid number.")


def random_otp():
    otp = random.randint(100000, 999999)

    print("\nGenerated OTP:", otp)


def random_sampling():
    data = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Watermelon"]

    try:
        size = int(input("\nEnter number of items to select: "))

        if size <= 0 or size > len(data):
            print("Please enter a valid sampling size.")
        else:
            sample = random.sample(data, size)

            print("Random Sample:", sample)

    except ValueError:
        print("Please enter a valid number.")


def game_simulation():
    print("\nGuess the Number Game")

    number = random.randint(1, 10)

    try:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Congratulations! You guessed correctly.")
        else:
            print("Wrong guess.")
            print("Correct number was:", number)

    except ValueError:
        print("Please enter a valid number.")


def random_menu():
    while True:
        print("\n==========================")
        print("Random Data Generation:")
        print("==========================")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling")
        print("6. Game Simulation")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            random_number()

        elif choice == "2":
            random_list()

        elif choice == "3":
            random_password()

        elif choice == "4":
            random_otp()

        elif choice == "5":
            random_sampling()

        elif choice == "6":
            game_simulation()

        elif choice == "7":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    random_menu()