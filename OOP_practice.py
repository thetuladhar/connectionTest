#CLASS
class Dog:
    #class attributes

    kind="Puppy"
    #initializer #breed,age,color,origin are attributes
    def __init__(self,breed,age,color,origin):
        #instance variable
        self.breed = breed
        self.age = age
        self.color = color
        self.origin = origin

    def bark(self):
        print("Woof Woof")

    def sleep(self):
        print("ZZZzzzz")


pug = Dog(breed="Pug",age=7,color="Beige",origin="America")
lab = Dog(breed="Lab",age=10,color="golden",origin="Asia")
chiwawaa = Dog("Chiwawa",5,"white",'Mexico')


#CAR EXAMPLE

class Car:
    #class variables
    wheels = 4
    def __init__(self,name):
        print("constructor was called")
        #instance variable
        self.name = name

    def makeNoise(self):
        print("Vroom Vroom")


muscle=Car(name="Mustang")
totoya=Car(name="Camry")

muscle.wheels=6
#print(totoya.wheels)




#object base by default
class Person(object):

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def __del__(self):
        pass

    def display(self):
        print(self.name,self.id)


person=Person("John","007")
person.display()

#SUPER METHOD and it should be the last line in the child init method