from abc import ABC, abstractmethod

class BankTransaction(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass

class SavingsAccount(BankTransaction):
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f"${amount} was deposited. New balance is ${self.balance}")
        else:
            print("Invalid Depoisit Amount")

    def withdraw(self,amount):
        if amount>0:
            if self.balance>=amount:
                self.balance=self.balance-amount
                print(f"${amount} was withdrawn. New balance is ${self.balance}")
            else:
                print("Insufficient Funds")

class CheckingAccount(BankTransaction):
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f"${amount} was deposited. New balance is ${self.balance}")
        else:
            print("Invalid Depoisit Amount")

    def withdraw(self,amount):
        if amount>0:
            if self.balance>=amount:
                self.balance=self.balance-amount
                print(f"${amount} was withdrawn. New balance is ${self.balance}")
            else:
                print("Insufficient Funds")

savings=SavingsAccount(5000)
savings.deposit(1000)
savings.withdraw(2000)

checking=CheckingAccount()
checking.deposit(1700)
checking.withdraw(200)

