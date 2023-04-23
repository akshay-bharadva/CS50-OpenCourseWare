from random import randint


def main():
    number = generateRandomInt(1, 100)
    print(number)


def generateRandomInt(a, b):
    return randint(a, b)


main()
