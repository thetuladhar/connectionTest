class Company:
    def __init__(self,revenue,profit,name,location):
        #private 
        self.__revenue = revenue
        self.__profit=profit
        #public 
        self.name=name
        self.location=location

    #methods to access peivate
    def get_revenue(self):
        return self.__revenue

    def get_profit(self):
        return self.__profit

class Employee(Company):
    def __init__(self,name,location,salary,bank_account_number):
        # Private members
        self.__salary = salary
        self.__bank_account_number = bank_account_number
        # Public members
        self.name = name
        self.location = location

    # Methods to access private members
    def get_salary(self):
        return self.__salary

    def get_bank_account_number(self):
        return self.__bank_account_number

company = Company(10000000, 2000000, "Tesla", "New York")
employee = Employee("Elon Musk", "New York", 1, "1234567890")

# Accessing and printing public members 
print("Company name:", company.name)
print("Employee name:", employee.name)
print("Employee location:", employee.location)

# Accessing and printing private members using methods
print("Company revenue:", company.get_revenue())
print("Company profit:", company.get_profit())
print("Employee salary:", employee.get_salary())
print("Employee bank account number:", employee.get_bank_account_number())