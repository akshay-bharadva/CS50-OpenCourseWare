class Student:
    def __init__(self, name, house):  # constructor
        if not name:
            raise ValueError("Missing name")
        if not house:
            raise ValueError("Missing house")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError(f"Invalid house")
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
