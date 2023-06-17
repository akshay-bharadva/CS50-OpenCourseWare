class Student:
    def __init__(self, name, house): # constructor
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = get_name()
    house = get_house()
    return Student(name, house)


def get_house():
    return input("House: ")


def get_name():
    return input("Name: ")


if __name__ == "__main__":
    main()
