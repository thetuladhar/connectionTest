import random

class BankAccount:
    def __init__(self):
        #Private attributes
        self._balance=0
        self._account_number=self._generate_account_number()

    def _generate_account_number(self): 
        return ''.join(str(random.randint(0, 9)) for _ in range(8))

    def deposit(self,amount):
        if amount>0:
            self._balance=self._balance+amount
            return f"Deposited Amount is {amount}.New Balance is {self._balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."
    def withdraw(self,amount):
        if amount>0:
            if self._balance>=amount:
                self._balance=self._balance-amount
                return f"Withdrawl Amount is {amount}.New Balance is {self._balance}"
            else:
                return "Insufficient Funds"
    def get_balace(self):
        return self._balance
    def get_account_number(self):
        return self._account_number


account=BankAccount()

print("Initial Balance ",account.get_balace())
print("Account Number ",account.get_account_number())

print(account.deposit(5000))#deposit 5000
print(account.withdraw(6000))#withdraw EXCESS
print(account.withdraw(2000))#withdraw 2000
print("Final Balance ",account.get_balace())





    

    

    

