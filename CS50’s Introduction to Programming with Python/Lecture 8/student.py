class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = get_name()
    student.house = get_house()
    return student


def get_house():
    return input("House: ")


def get_name():
    return input("Name: ")


if __name__ == "__main__":
    main()
