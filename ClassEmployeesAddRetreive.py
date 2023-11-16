class Employee:
  #empty employee list
  employees=[]

  def __init__(self,name,number):
    self.name=name
    self.number=number

  def get_info(self):
    return {self.name,self.number}
  
  def add_employee(self):
    self.employees.append(self.get_info())

def main():
  while True:
    #print options
    print("1 to add employee")
    print("2 to view all employees")
    print("0 to exit")

    entry=int(input("Enter your option : "))
    #exit
    if entry == 0:
      print("Exiting Application!")
      break
    #input employee
    elif entry == 1:
      name = input("Enter employee name: ")
      id = int(input("Enter employee ID: "))
      employee = Employee(name, id)
      employee.add_employee()
    #show employees
    elif entry ==2:
      print("EMPLOYEE LIST")
      for row in Employee.employees:
        print(row)
 

if __name__ == "__main__":
  main()