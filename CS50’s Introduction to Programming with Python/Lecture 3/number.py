def main():
    label = "What's value of x? "
    x = get_int(label)
    print(f"x is {x}")


def get_int(label):
    while True:
        try:
            return int(input(label))
        except ValueError:
            # pass silently ignore
            pass
            # print("x is not integer")


main()
