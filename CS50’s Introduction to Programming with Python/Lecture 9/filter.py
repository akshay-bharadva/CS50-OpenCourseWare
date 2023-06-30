numbers = [10, 12, 45, 34, 56, 25, 78, 45, 15, 35, 65, 20]

# adults = [
#     number for number in numbers if number > 18
# ]


def is_adult(age):
    return age > 18


# adults = filter(is_adult, numbers)
adults = filter(lambda age: age > 18, numbers)

print("adults:", sorted(adults))
