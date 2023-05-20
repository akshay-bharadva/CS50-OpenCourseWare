import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, study in reader:
        student = {
            "name":name,
            "study":study
        }
        students.append(student)

for student in sorted(students, key=lambda param: param["name"]):
    print(f"{student['name']} studied {student['study']}")
