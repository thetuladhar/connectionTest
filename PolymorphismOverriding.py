class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 6000  # Managers get a $5000 raise

class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 5000  # Developers get a $3000 raise

class Designer(Employee):
    def calculate_salary(self):
        return self.salary + 2000  # Designers get a $2000 raise


manager = Manager("John", 60000)
developer = Developer("Alice", 50000)
designer = Designer("Bob", 45000)


print(f"{manager.name}'s salary: ${manager.calculate_salary()}")
print(f"{developer.name}'s salary: ${developer.calculate_salary()}")
print(f"{designer.name}'s salary: ${designer.calculate_salary()}")