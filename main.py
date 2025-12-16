def main():
    name = input("Please enter your name: ").strip()

    if not name:
        print("invalid name")
        return

    print({"message":f"Hello, {name}!"})

if __name__ == "__main__":
    main()
