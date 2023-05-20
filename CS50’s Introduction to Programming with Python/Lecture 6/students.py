import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        student = {
            "name":row["name"],
            "study":row["study"]
        }
        students.append(student)

for student in sorted(students, key=lambda param: param["name"]):
    print(f"{student['name']} studied {student['study']}")
