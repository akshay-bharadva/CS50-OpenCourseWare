students = []

with open("students.csv") as file:
    for line in file:
        name, study = line.rstrip().split(",")
        student = {
            "name":name,
            "study":study
        }
        students.append(student)

for student in students:
    print(f"{student['name']} studied {student['study']}")
