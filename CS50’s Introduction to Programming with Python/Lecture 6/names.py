file_name = "names.txt"


def main():
    write_to_file()


def write_to_file():
    name = input("What's your name? ")

    with open(file_name, "a") as file:
        file.write(f"{name}\n")


if __name__ == "__main__":
    main()
