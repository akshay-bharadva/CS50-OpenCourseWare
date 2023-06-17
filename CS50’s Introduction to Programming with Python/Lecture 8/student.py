def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = get_name()
    house = get_house()
    return name, house


def get_house():
    return input("House: ")


def get_name():
    return input("Name: ")


if __name__ == "__main__":
    main()
