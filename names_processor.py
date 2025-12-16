from typing import Dict,List

class InvalidNameError(Exception):
    pass

def parse_names(raw_input: str) -> List[str]:
    """
    Accepts comas seperated names and cleaned list
    """
    names = [name.strip() for name in raw_input.split(',')]
    return names

def validate_names(names: List[str]) -> None:
    for name in names:
        if not name:
            raise InvalidNameError("cannot be empty")
        if not name.isalpha():
            raise InvalidNameError("name must contain only letters")

def build_response(name: str) -> Dict:
    unique_names = list(set(name))
    return {
        "count": len(unique_names),
        "names": unique_names,
    }

def main():
    raw_input_data = input("enter comma seperated names")

    try:
        names = parse_names(raw_input_data)
        validate_names(names)
        response = build_response(names)
        print(response)

    except InvalidNameError as e:
        print({"error": str(e)})

if __name__ == "__main__":
    main()


