students = []

with open("students.csv") as file:
    for line in file:
        name, study = line.rstrip().split(",")
        student = {
            "name":name,
            "study":study
        }
        students.append(student)

for student in sorted(students, key=lambda param: param["name"]):
    print(f"{student['name']} studied {student['study']}")
