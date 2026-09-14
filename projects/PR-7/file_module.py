def create_file():
    filename = input("\nEnter file name: ")

    try:
        with open(filename, "x") as file:
            file.write("")

        print("File created successfully!")

    except FileExistsError:
        print("File already exists.")

    except OSError:
        print("Unable to create file.")


def write_file():
    filename = input("\nEnter file name: ")
    data = input("Enter data to write: ")

    try:
        with open(filename, "w") as file:
            file.write(data)

        print("Data written successfully!")

    except OSError:
        print("Unable to write to file.")


def read_file():
    filename = input("\nEnter file name: ")

    try:
        with open(filename, "r") as file:
            data = file.read()

        print("\nFile Content:")
        print(data)

    except FileNotFoundError:
        print("File not found.")

    except OSError:
        print("Unable to read file.")


def append_file():
    filename = input("\nEnter file name: ")
    data = input("Enter data to append: ")

    try:
        with open(filename, "a") as file:
            file.write("\n" + data)

        print("Data appended successfully!")

    except OSError:
        print("Unable to append data.")


def file_menu():
    while True:
        print("\n==========================")
        print("File Operations:")
        print("==========================")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            write_file()

        elif choice == "3":
            read_file()

        elif choice == "4":
            append_file()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    file_menu()