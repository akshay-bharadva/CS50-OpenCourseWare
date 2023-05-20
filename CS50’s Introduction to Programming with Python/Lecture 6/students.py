students = []

with open("students.csv") as file:
    for line in file:
        name, study = line.rstrip().split(",")
        student = {
            name,
            study
        }
        students.append(student)

print(students)
