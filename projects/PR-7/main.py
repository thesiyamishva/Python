from datetime_module import datetime_menu
from math_module import math_menu
from random_module import random_menu
from uuid_module import uuid_menu
from file_module import file_menu
from explorer import explore_module


def main():
    while True:
        print("\n==========================")
        print("Welcome to Multi-Utility Toolkit")
        print("==========================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_menu()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("\n==========================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("==========================")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()