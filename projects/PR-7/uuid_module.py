import uuid


def uuid_menu():
    print("\n==========================")
    print("Generate Unique Identifiers:")
    print("==========================")

    unique_id = uuid.uuid4()

    print("Generated UUID:", unique_id)

    print("==========================")