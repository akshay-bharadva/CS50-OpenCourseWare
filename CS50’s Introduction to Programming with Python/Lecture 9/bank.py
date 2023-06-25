class Account:
    def __init__(self):
        self.balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def deposit(self, n):
        self.balance += n

    def withdraw(self, n):
        self.balance -= n


def main():
    account = Account()
    print(f"Balance: {account.balance}")
    account.deposit(100)
    account.withdraw(50)
    print(f"Balance: {account.balance}")


if __name__ == "__main__":
    main()
