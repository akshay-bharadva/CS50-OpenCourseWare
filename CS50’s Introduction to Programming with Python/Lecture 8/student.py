def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = get_name()
    house = get_house()
    return name, house # returning tuple and it's immutable


def get_house():
    return input("House: ")


def get_name():
    return input("Name: ")


if __name__ == "__main__":
    main()
