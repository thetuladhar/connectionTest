class Base1(object):
    def __init__(self):
        self.str1="Geek1"
        print("Base1")

class Base2(object):
    def __init__(self):
        self.str2="Geek2"
        print("Base2")
    

class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1,self.str2)

print(Derived.__mro__)#Python ues the MRO behind the scenes

ob=Derived()
ob.printStrs()