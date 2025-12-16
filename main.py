def get_name() -> str:
    name = input("Please enter your name: ")
    return name


def validate_name(name: str) -> bool:
    if not name:
        return False
    return name.isalpha()

def build_response(name: str) -> dict:
    return {"message" : f"Hello {name}"}

def build_error(message: str) -> dict:
    return {"error": message}

def main():
    name = get_name()

    if not validate_name(name):
        print(build_error("Invalid name. Only alphabetic characters allowed."))

        return
    response = build_response(name)
    print(response)

if __name__ == "__main__":
    main()
