import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sales_analyzer import SalesDataAnalyzer  

def main():
    analyzer = None

    while True:
        print("\n=========== Data Analysis & Visualization Program ===========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Clean Data")
        print("4. Mathematical Operations")
        print("5. Aggregate Functions")
        print("6. Statistical Analysis")
        print("7. Pivot Table")
        print("8. Visualize Data")
        print("9. Exit")
        print("============================================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter dataset path (CSV file): ")
            analyzer = SalesDataAnalyzer(path)

        elif choice == "2" and analyzer:
            analyzer.explore_data()

        elif choice == "3" and analyzer:
            analyzer.clean_data()

        elif choice == "4" and analyzer:
            analyzer.mathematical_operations()

        elif choice == "5" and analyzer:
            analyzer.aggregate_functions()

        elif choice == "6" and analyzer:
            analyzer.statistical_analysis()

        elif choice == "7" and analyzer:
            analyzer.create_pivot_table()

        elif choice == "8" and analyzer:
            analyzer.visualize_data()

        elif choice == "9":
            print("Exiting program... Bye!")
            break

        else:
            print("Invalid choice or dataset not loaded!")

if __name__ == "__main__":
    main()
