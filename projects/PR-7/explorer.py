import math
import random
import datetime


def explore_module():
    print("\n==========================")
    print("Explore Module Attributes:")
    print("==========================")

    module_name = input("Enter module name to explore: ")

    modules = {
        "math": math,
        "random": random,
        "datetime": datetime
    }

    if module_name in modules:
        module = modules[module_name]

        print("\nAvailable Attributes in", module_name, "module:")
        print(dir(module))

    else:
        print("Module not available.")


if __name__ == "__main__":
    explore_module()