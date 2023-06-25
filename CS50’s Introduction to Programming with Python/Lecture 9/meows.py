import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, default=1, help="meow n times")
args = parser.parse_args()


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


if __name__ == "__main__":
    meows = meow(args.n)
    print(meows)
