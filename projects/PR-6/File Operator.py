from datetime import datetime
import os

class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry:\n")

            if not entry.strip():
                print("Journal entry cannot be empty.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            data = f"[{timestamp}]\n{entry}\n\n"

            try:
                with open(self.filename, "x") as file:
                    file.write(data)

            except FileExistsError:
                
                with open(self.filename, "a") as file:
                    file.write(data)

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied. Cannot write to the journal file.")

        except OSError as e:
            print("Error while writing to file:", e)

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

                if not content.strip():
                    print("\nNo journal entries found. Start by adding a new entry!")
                    return

                print("\nYour Journal Entries:")
                print("------------------------------")
                print(content)

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("\nError: Permission denied. Cannot read the journal file.")

    def search_entry(self):
        keyword = input("\nEnter a keyword or date to search: ")

        if not keyword.strip():
            print("Search keyword cannot be empty.")
            return

        try:
            with open(self.filename, "r") as file:
                content = file.read()

                if not content.strip():
                    print("\nNo journal entries found.")
                    return

                entries = content.strip().split("\n\n")
                found = []

                for entry in entries:
                    if keyword.lower() in entry.lower():
                        found.append(entry)

                if found:
                    print("\nMatching Entries:")
                    print("------------------------------")

                    for entry in found:
                        print(entry)
                        print()

                else:
                    print(f"\nNo entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("\nError: Permission denied. Cannot read the journal file.")

    def delete_all_entries(self):
        if not os.path.exists(self.filename):
            print("\nNo journal entries to delete.")
            return

        confirmation = input("\nAre you sure you want to delete all entries? (yes/no): ")

        if confirmation.lower() == "yes":
            try:
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")

            except PermissionError:
                print("\nError: Permission denied. Cannot delete the journal file.")

            except OSError as e:
                print("\nError while deleting file:", e)

        else:
            print("\nDelete operation cancelled.")

def main():
    journal = JournalManager()

    print("\nWelcome to Personal Journal Manager!")

    while True:
        print("\nPlease select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nUser Input: ")

        if choice == "1":
            journal.add_entry()

            journal.view_entries()

        elif choice == "3":
            journal.search_entry()

        elif choice == "4":
            journal.delete_all_entries()

        elif choice == "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("\nInvalid option. Please select a valid option from the menu.")

main()