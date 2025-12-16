from typing import List

class InvalidNameError(Exception):
    pass

def read_names_from_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def validate_names(name: str) -> None:
    ...

def process_names(names: List[str]) -> None:
    ...




def write_output(file_path: str, data: List[str]) -> None:
    ...


def main():
    names = read_names_from_file("input_names.txt")
    process_names(names)
    print("Processing complete. Check output files.")


if __name__ == "__main__":
    main()





