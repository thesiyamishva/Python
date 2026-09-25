import numpy as np

class DataAnalytics:
    total_objects = 0

    def __init__(self, array=None):
        self.__array = np.array(array) if array is not None else None
        DataAnalytics.total_objects += 1

    @classmethod
    def from_list(cls, data):
        return cls(np.array(data))

    @staticmethod
    def show_title(title):
        print("\n" + "=" * 45)
        print(title)
        print("=" * 45)

    def __check_array(self):
        if self.__array is None:
            print("Please create an array first.")
            return False
        return True

    def __read_elements(self, count):
        while True:
            try:
                values = list(map(float, input(f"Enter {count} elements separated by space: ").split()))

                if len(values) != count:
                    print(f"Please enter exactly {count} elements.")
                    continue

                if all(x.is_integer() for x in values):
                    return np.array(values, dtype=int)

                return np.array(values)

            except ValueError:
                print("Please enter valid numbers.")

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        while True:
            try:
                choice = int(input("Enter your choice: "))

                if choice in (1, 2, 3):
                    break

                print("Enter 1, 2, or 3.")

            except ValueError:
                print("Please enter a valid choice.")

        if choice == 1:
            while True:
                try:
                    n = int(input("Enter the number of elements: "))

                    if n > 0:
                        break

                    print("Enter a positive number.")

                except ValueError:
                    print("Please enter a valid number.")

            self.__array = self.__read_elements(n)

        elif choice == 2:
            while True:
                try:
                    rows = int(input("Enter the number of rows: "))
                    cols = int(input("Enter the number of columns: "))

                    if rows > 0 and cols > 0:
                        break

                    print("Rows and columns must be positive.")

                except ValueError:
                    print("Please enter valid numbers.")

            self.__array = self.__read_elements(rows * cols)
            self.__array = self.__array.reshape(rows, cols)

        else:
            while True:
                try:
                    depth = int(input("Enter the number of layers: "))
                    rows = int(input("Enter the number of rows: "))
                    cols = int(input("Enter the number of columns: "))

                    if depth > 0 and rows > 0 and cols > 0:
                        break

                    print("All dimensions must be positive.")

                except ValueError:
                    print("Please enter valid numbers.")

            self.__array = self.__read_elements(depth * rows * cols)
            self.__array = self.__array.reshape(depth, rows, cols)

        print("\nArray created successfully:")
        print(self.__array)

    def array_management(self):
        if not self.__check_array():
            return

        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    if self.__array.ndim == 1:
                        index = int(input("Enter index: "))
                        print("Value:", self.__array[index])

                    elif self.__array.ndim == 2:
                        row = int(input("Enter row index: "))
                        col = int(input("Enter column index: "))
                        print("Value:", self.__array[row, col])

                    else:
                        layer = int(input("Enter layer index: "))
                        row = int(input("Enter row index: "))
                        col = int(input("Enter column index: "))
                        print("Value:", self.__array[layer, row, col])

                except (ValueError, IndexError):
                    print("Invalid index.")

            elif choice == "2":
                try:
                    if self.__array.ndim == 1:
                        value = input("Enter range (start:end): ")
                        start, end = value.split(":")
                        start = int(start) if start else None
                        end = int(end) if end else None
                        result = self.__array[start:end]

                    elif self.__array.ndim == 2:
                        rows = input("Enter the row range (start:end): ")
                        cols = input("Enter the column range (start:end): ")

                        rs, re = rows.split(":")
                        cs, ce = cols.split(":")

                        rs = int(rs) if rs else None
                        re = int(re) if re else None
                        cs = int(cs) if cs else None
                        ce = int(ce) if ce else None

                        result = self.__array[rs:re, cs:ce]

                    else:
                        layers = input("Enter the layer range (start:end): ")
                        rows = input("Enter the row range (start:end): ")
                        cols = input("Enter the column range (start:end): ")

                        ls, le = layers.split(":")
                        rs, re = rows.split(":")
                        cs, ce = cols.split(":")

                        ls = int(ls) if ls else None
                        le = int(le) if le else None
                        rs = int(rs) if rs else None
                        re = int(re) if re else None
                        cs = int(cs) if cs else None
                        ce = int(ce) if ce else None

                        result = self.__array[ls:le, rs:re, cs:ce]

                    print("\nSliced Array:")
                    print(result)

                except (ValueError, IndexError):
                    print("Invalid range.")

            elif choice == "3":
                break

            else:
                print("Invalid choice.")

    def mathematical_operations(self):
        if not self.__check_array():
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")
        print("7. Go Back")

        choice = input("Enter your choice: ")

        if choice == "7":
            return

        if choice in ("1", "2", "3", "4"):
            try:
                second = self.__read_elements(self.__array.size).reshape(self.__array.shape)

                print("\nOriginal Array:")
                print(self.__array)

                print("\nSecond Array:")
                print(second)

                if choice == "1":
                    result = self.__array + second
                    name = "Addition"

                elif choice == "2":
                    result = self.__array - second
                    name = "Subtraction"

                elif choice == "3":
                    result = self.__array * second
                    name = "Multiplication"

                else:
                    if np.any(second == 0):
                        print("Division by zero is not allowed.")
                        return

                    result = self.__array / second
                    name = "Division"

                print(f"\nResult of {name}:")
                print(result)

            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            if self.__array.ndim != 2:
                print("Dot product requires a 2D array.")
                return

            try:
                rows = int(input("Enter number of rows for second array: "))
                cols = int(input("Enter number of columns for second array: "))

                second = self.__read_elements(rows * cols).reshape(rows, cols)

                if self.__array.shape[1] != second.shape[0]:
                    print("Invalid dimensions for dot product.")
                    return

                print("\nSecond Array:")
                print(second)

                print("\nDot Product:")
                print(np.dot(self.__array, second))

            except ValueError:
                print("Invalid input.")

        elif choice == "6":
            if self.__array.ndim != 2:
                print("Matrix multiplication requires a 2D array.")
                return

            try:
                rows = int(input("Enter number of rows for second matrix: "))
                cols = int(input("Enter number of columns for second matrix: "))

                second = self.__read_elements(rows * cols).reshape(rows, cols)

                if self.__array.shape[1] != second.shape[0]:
                    print("Invalid dimensions for matrix multiplication.")
                    return

                print("\nSecond Matrix:")
                print(second)

                print("\nMatrix Multiplication:")
                print(self.__array @ second)

            except ValueError:
                print("Invalid input.")

        else:
            print("Invalid choice.")

    def combine_split(self):
        if not self.__check_array():
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        print("3. Go Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                second = self.__read_elements(self.__array.size).reshape(self.__array.shape)

                print("\nOriginal Array:")
                print(self.__array)

                print("\nSecond Array:")
                print(second)

                if self.__array.ndim == 1:
                    result = np.concatenate((self.__array, second))
                    print("\nCombined Array:")
                    print(result)

                else:
                    result = np.concatenate((self.__array, second), axis=0)
                    print("\nCombined Array (Vertical Stack):")
                    print(result)

            except ValueError:
                print("Invalid input.")

        elif choice == "2":
            try:
                parts = int(input("Enter number of parts: "))

                if self.__array.ndim == 1:
                    result = np.array_split(self.__array, parts)

                else:
                    axis = int(input("Enter axis (0 for rows, 1 for columns): "))

                    if axis not in (0, 1):
                        print("Axis must be 0 or 1.")
                        return

                    result = np.array_split(self.__array, parts, axis=axis)

                print("\nSplit Arrays:")

                for i, item in enumerate(result, 1):
                    print(f"Part {i}:")
                    print(item)

            except (ValueError, IndexError):
                print("Invalid input.")

        elif choice == "3":
            return

        else:
            print("Invalid choice.")

    def search_sort_filter(self):
        if not self.__check_array():
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        print("4. Go Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                value = float(input("Enter value to search: "))
                positions = np.argwhere(self.__array == value)

                if len(positions) == 0:
                    print("Value not found.")
                else:
                    print("Value found at index/indices:")
                    print(positions)

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            print("\nOriginal Array:")
            print(self.__array)

            order = input("Enter order (1 for ascending, 2 for descending): ")

            if order == "1":
                result = np.sort(self.__array, axis=-1)

            elif order == "2":
                result = np.sort(self.__array, axis=-1)[..., ::-1]

            else:
                print("Invalid order.")
                return

            print("\nSorted Array:")
            print(result)
            print("(Sorting applied row-wise.)")

        elif choice == "3":
            try:
                condition = input("Filter condition (>, <, >=, <=, ==, !=): ")
                value = float(input("Enter value: "))

                if condition == ">":
                    result = self.__array[self.__array > value]

                elif condition == "<":
                    result = self.__array[self.__array < value]

                elif condition == ">=":
                    result = self.__array[self.__array >= value]

                elif condition == "<=":
                    result = self.__array[self.__array <= value]

                elif condition == "==":
                    result = self.__array[self.__array == value]

                elif condition == "!=":
                    result = self.__array[self.__array != value]

                else:
                    print("Invalid condition.")
                    return

                print("\nFiltered Values:")
                print(result)

            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            return

        else:
            print("Invalid choice.")

    def aggregates_statistics(self):
        if not self.__check_array():
            return

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentiles")
        print("9. Correlation Coefficient")
        print("10. Go Back")

        choice = input("Enter your choice: ")

        print("\nOriginal Array:")
        print(self.__array)

        if choice == "1":
            print("Sum of Array:", np.sum(self.__array))

        elif choice == "2":
            print("Mean of Array:", np.mean(self.__array))

        elif choice == "3":
            print("Median of Array:", np.median(self.__array))

        elif choice == "4":
            print("Standard Deviation:", np.std(self.__array))

        elif choice == "5":
            print("Variance:", np.var(self.__array))

        elif choice == "6":
            print("Minimum Value:", np.min(self.__array))

        elif choice == "7":
            print("Maximum Value:", np.max(self.__array))

        elif choice == "8":
            try:
                p = float(input("Enter percentile (0-100): "))

                if 0 <= p <= 100:
                    print(f"{p}th Percentile:", np.percentile(self.__array, p))
                else:
                    print("Percentile must be between 0 and 100.")

            except ValueError:
                print("Invalid percentile.")

        elif choice == "9":
            try:
                first = self.__array.flatten()
                second = self.__read_elements(len(first))

                correlation = np.corrcoef(first, second)[0, 1]

                print("\nSecond Array:")
                print(second)
                print("Correlation Coefficient:", correlation)

            except ValueError:
                print("Invalid input.")

        elif choice == "10":
            return

        else:
            print("Invalid choice.")


def main():
    DataAnalytics.show_title("Welcome to the NumPy Analyzer!")

    analyzer = DataAnalytics()

    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Array Indexing and Slicing")
        print("3. Perform Mathematical Operations")
        print("4. Combine or Split Arrays")
        print("5. Search, Sort, or Filter Arrays")
        print("6. Compute Aggregates and Statistics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.create_array()

        elif choice == "2":
            analyzer.array_management()

        elif choice == "3":
            analyzer.mathematical_operations()

        elif choice == "4":
            analyzer.combine_split()

        elif choice == "5":
            analyzer.search_sort_filter()

        elif choice == "6":
            analyzer.aggregates_statistics()

        elif choice == "7":
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()