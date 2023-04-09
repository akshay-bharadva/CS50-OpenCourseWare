# / * + - %
def main():
    x = int(input("What's x? "))
    print(even_or_odd(x))


def even_or_odd(x):
    if x % 2 == 0:
        return f"{x} is even number..."
    else:
        return f"{x} is odd number..."


main()
