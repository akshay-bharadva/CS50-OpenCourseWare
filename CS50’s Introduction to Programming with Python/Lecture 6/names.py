file_name = "names.txt"


def main():
    # write_to_file()
    read_file()


def write_to_file():
    name = input("What's your name? ")

    with open(file_name, "a") as file:
        file.write(f"{name}\n")


def read_file():
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(f"hello, {line.rstrip()}")

if __name__ == "__main__":
    main()
