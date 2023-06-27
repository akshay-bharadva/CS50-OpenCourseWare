numbers = [10, 12, 45, 34, 56, 25, 78, 45, 15, 35, 65, 20]

adults = [
    number for number in numbers if number > 18
]

print("adults:", sorted(adults))
