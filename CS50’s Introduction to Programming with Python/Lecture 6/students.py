students = []

with open("students.csv") as file:
    for line in file:
        name, study = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["study"] = study
        students.append(student)

print(students)
