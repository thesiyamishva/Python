def create_log(filename, message):
    try:
        with open(filename, "a") as file:
            file.write(message + "\n")

        return True

    except OSError:
        return False


def read_log(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        return "File not found."