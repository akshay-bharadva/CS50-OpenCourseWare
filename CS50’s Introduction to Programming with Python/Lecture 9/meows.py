import sys


def meow(n: int) -> str:
    """
    Meow n times

    :param n: Number of times to Meow
    :type n: int
    :raise TypeError: If n is not int
    :return: A str with n times meow
    :rtype: str
    """
    return "meow " * n


if len(sys.argv) == 1:
    meows: str = meow(1)
    print(meows)
if len(sys.argv) == 3 and sys.argv[1] == "-n":
    meows: str = meow(int(sys.argv[2]))
    print(meows)
else:
    number: int = int(input("Number: ").strip())
    meows: str = meow(number)
    print(meows)
