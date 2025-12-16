from typing import List

class InvalidNameError(Exception):
    pass

def read_names_from_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def validate_names(name: str) -> None:
    if not name:
        raise InvalidNameError("cannot be empty")
    if not name.isalpha():
        raise InvalidNameError(f"name must only contain letters{name}")

def process_names(names: List[str]) -> None:
    valid_names = []
    errors = []

    for name in names:
        try:
            validate_names(name)
            valid_names.append(name)
        except InvalidNameError as e:
            errors.append(str(e))

    write_output("valid_names.txt", valid_names)
    write_output("errors.txt", errors)

def write_output(file_path: str, data: List[str]) -> None:
    with open(file_path, "w") as file:
        for item in data:
            file.write(item + "\n")


def main():
    names = read_names_from_file("input_names.txt")
    process_names(names)
    print("Processing complete. Check output files.")


if __name__ == "__main__":
    main()





