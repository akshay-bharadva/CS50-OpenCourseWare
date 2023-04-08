def main():
    meow(get_number())


def get_number():
    while True:
        i = int(input("What's i? "))
        if i > 0:
            return i


def meow(i):
    for _ in range(i):
        print("meow")


main()
