'''emptyList=[]
for i in range(5):
    number=input("Enter a username :")
    emptyList.append(number)

print(set(emptyList))'''



#Alternative Code
'''UsernameList=[]
number1=input("Enter a username :")
UsernameList.append(number1)
number2=input("Enter a username :")
UsernameList.append(number2)
number3=input("Enter a username :")
UsernameList.append(number3)
number4=input("Enter a username :")
UsernameList.append(number4)
number5=input("Enter a username :")
UsernameList.append(number5)
print(set(UsernameList))'''

#SET answer

number1=input("Enter a username :")
number2=input("Enter a username :")
number3=input("Enter a username :")

mtset=set()
mtset.add(number1)
mtset.add(number2)
mtset.add(number3)

print(mtset)
