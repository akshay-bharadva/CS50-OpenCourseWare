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


number: int = int(input("Number: ").strip())
meows: str = meow(number)
print(meows)
