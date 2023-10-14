list1=[0,1,2,3,4,5]
print("Enter two numbers to swap indexes")
print(list1)

num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))

list1[num1],list1[num2]=list1[num2],list1[num1]

print(list1)