def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_house():
    return input("House: ")


def get_name():
    return input("Name: ")


if __name__ == "__main__":
    main()
