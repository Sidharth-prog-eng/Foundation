class InvalidNameError(Exception):
    pass

def get_name() -> str:
    name = input("Please enter your name: ")
    return name


def validate_name(name: str) -> bool:
    if not name:
        raise InvalidNameError("Name cannot be empty.")

    if not name.isalpha():
        raise InvalidNameError("Name must be alphabetic.")


def build_response(name: str) -> dict:
    return {"message" : f"Hello {name}"}

def build_error(message: str) -> dict:
    return {"error": message}

def main():
    try:
        name = get_name()
        validate_name(name)
        print(build_response(name))
    except InvalidNameError as e:
        print(build_error(str(e)))

if __name__ == "__main__":
    main()
