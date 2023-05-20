with open("students.csv") as file:
    for line in file:
        name, study = line.rstrip().split(",")
        print(f"{name} studied {study}")