students = ["Ron", "Harry"]

# gryffindors = {student: "Grayffindor" for student in students}

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# for i in range(len(students)):
#     print(i+1, students[i])

for i, student in enumerate(students,start=1):
    print(i, student)

# print(gryffindors)
