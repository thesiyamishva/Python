print("Welcome To Student Data Organizer")

Student = []

while True:
    print("\n Select an option :\n")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("\n Enter your choice : "))

    match choice:

        case 1:
            print("\n Enter Student Details")

            st = {
                "Student Id": len(Student) + 1,
                "Name": input("Name : "),
                "Age": int(input("Age : ")),
                "Grade": input("Grade : "),
                "DOB": input("Date Of Birth (YYYY-MM-DD) : "),
                "Subjects": set(input("Subjects (comma-separated) : ").split(","))
            }

            Student.append(st)

            print("\n Student Added Successfully!")

        case 2:
            if len(Student) == 0:
                print("\n No Student Records Found!")
            else:
                print("\n Student Records:\n")

                for st in Student:
                    print(
                        f"Student Id : {st['Student Id']} | "
                        f"Name : {st['Name']} | "
                        f"Age : {st['Age']} | "
                        f"Grade : {st['Grade']} | "
                        f"DOB : {st['DOB']} | "
                        f"Subjects : {', '.join(st['Subjects'])}"
                    )
        
        case 3:
            stid = int(input("Enter Student Id to Update : "))
            found = False

            for st in Student:
                if st["Student Id"] == stid:
                    found = True

                    st["Name"] = input("Enter New Name : ")
                    st["Age"] = int(input("Enter New Age : "))
                    st["Grade"] = input("Enter New Grade : ")
                    st["DOB"] = input("Enter New DOB (YYYY-MM-DD) : ")
                    st["Subjects"] = set(
                        input("Enter New Subjects (comma-separated) : ").split(",")
                    )

                    print("\n Student Record Updated Successfully!")
                    break

            if found == False:
                print("\n Sorry! Student Id not found!")

        case 4:
            delid = int(input("Enter Student Id to Delete : "))
            found = False

            for st in Student:
                if st["Student Id"] == delid:
                    Student.remove(st)
                    found = True

                    print("\n Student Record Deleted Successfully!")
                    break

            if found == False:
                print("\n Sorry! Student Id not found!")

        case 5:
            all_subjects = set()

            for st in Student:
                all_subjects |= st["Subjects"]

            if len(all_subjects) == 0:
                print("\nNo Subjects Found!")
            else:
                print("\nSubjects Offered:")
                for subject in sorted(all_subjects):
                    print(subject)

        case 6:
            print("\n Thank you for using Student Data Organizer. Goodbye!")
            break

       
        case _:
            print("\n Invalid Choice! Please enter a number between 1 and 6.")