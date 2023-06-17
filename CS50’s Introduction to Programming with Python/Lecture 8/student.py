class Student:
    def __init__(self, name, house):  # constructor
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if not house:
            raise ValueError("Missing house")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError(f"Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


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
