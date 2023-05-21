import csv

file_name = "students.csv"


def main():
    # read_csv()
    write_csv()


def write_csv():
    name = input("What's your name? ")
    study = input("What you study? ")

    with open(file_name, "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "study"])
        writer.writerow({"name": name, "study": study})


def read_csv():
    students = []

    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = {
                "name": row["name"],
                "study": row["study"]
            }
            students.append(student)

    for student in sorted(students, key=lambda param: param["name"]):
        print(f"{student['name']} studied {student['study']}")


if __name__ == "__main__":
    main()
