class Person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)

customer=Person("Johnny","007")

#customer.display()

class Emp(Person):
    
    def __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post
        #name and id from the parent class
        #super should be th elast line
        super().__init__(name,id)

    def printer(self):
        print("EMP class called")


#employee1=Emp("Steve","001")
employee2=Emp("Johnny",10,10000,'Contract')

employee2.display()
#employee2.printer()
