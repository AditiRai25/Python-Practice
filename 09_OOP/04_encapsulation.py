# Demonstrate encapsulation using a private variable

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print("Balance:", account.get_balance())
