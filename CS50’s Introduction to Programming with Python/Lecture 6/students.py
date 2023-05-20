students = []

with open("students.csv") as file:
    for line in file:
        name, study = line.rstrip().split(",")
        student = {
            "name":name,
            "study":study
        }
        students.append(student)

def get_name(student):
    return student['name']

for student in sorted(students, key=get_name):
    print(f"{student['name']} studied {student['study']}")
