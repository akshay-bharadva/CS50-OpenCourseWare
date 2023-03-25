def main():
    great()
    name = input("What's your name? ")
    great(name)


def great(name='Developer'):
    print(f"Good Day, {name}!")


main()
