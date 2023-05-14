file_name = "names.txt"
names = []


def main():
    # write_to_file()
    read_file()


def write_to_file():
    name = input("What's your name? ")

    with open(file_name, "a") as file:
        file.write(f"{name}\n")


def read_file():
    with open(file_name, "r") as file:
        for line in file:
            names.append(line.rstrip())

    for name in sorted(names):
        print(f"hello, {name}")


if __name__ == "__main__":
    main()
