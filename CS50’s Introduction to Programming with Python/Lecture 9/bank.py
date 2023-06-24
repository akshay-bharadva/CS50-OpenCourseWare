balance = 0


def main():
    print(f"Balance: {balance}")
    deposite(100)
    withdrawn(50)
    print(f"Balance: {balance}")


def deposite(n):
    balance += n


def withdrawn(n):
    balance -= n


if __name__ == "__main__":
    main()
