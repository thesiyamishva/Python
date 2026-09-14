import math


def factorial():
    try:
        number = int(input("\nEnter a number: "))

        if number < 0:
            print("Factorial is not possible for negative numbers.")
        else:
            print("Factorial:", math.factorial(number))

    except ValueError:
        print("Please enter a valid integer.")


def compound_interest():
    try:
        principal = float(input("\nEnter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time = float(input("Enter time (in years): "))

        amount = principal * (1 + rate / 100) ** time
        interest = amount - principal

        print("Compound Interest:", round(amount, 2))

    except ValueError:
        print("Please enter valid numbers.")


def trigonometric_calculation():
    try:
        angle = float(input("\nEnter angle in degrees: "))

        radians = math.radians(angle)

        print("Sin:", round(math.sin(radians), 4))
        print("Cos:", round(math.cos(radians), 4))
        print("Tan:", round(math.tan(radians), 4))

    except ValueError:
        print("Please enter a valid number.")


def area_shapes():
    print("\nArea of Geometric Shapes")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            radius = float(input("Enter radius: "))

            area = math.pi * radius * radius

            print("Area of Circle:", round(area, 2))

        elif choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            area = length * width

            print("Area of Rectangle:", round(area, 2))

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            area = 0.5 * base * height

            print("Area of Triangle:", round(area, 2))

        elif choice == "4":
            side = float(input("Enter side: "))

            area = side * side

            print("Area of Square:", round(area, 2))

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numbers.")


def logarithm():
    try:
        number = float(input("\nEnter a positive number: "))

        if number <= 0:
            print("Number must be positive.")
        else:
            print("Natural Log:", round(math.log(number), 4))
            print("Log Base 10:", round(math.log10(number), 4))

    except ValueError:
        print("Please enter a valid number.")


def arithmetic_operations():
    try:
        a = float(input("\nEnter first number: "))
        b = float(input("Enter second number: "))

        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Multiplication:", a * b)

        if b != 0:
            print("Division:", a / b)
            print("Modulus:", a % b)
        else:
            print("Division: Cannot divide by zero")
            print("Modulus: Cannot divide by zero")

        print("Power:", a ** b)

    except ValueError:
        print("Please enter valid numbers.")


def math_menu():
    while True:
        print("\n==========================")
        print("Mathematical Operations:")
        print("==========================")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Logarithmic Calculations")
        print("6. Arithmetic Operations")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            factorial()

        elif choice == "2":
            compound_interest()

        elif choice == "3":
            trigonometric_calculation()

        elif choice == "4":
            area_shapes()

        elif choice == "5":
            logarithm()

        elif choice == "6":
            arithmetic_operations()

        elif choice == "7":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    math_menu()