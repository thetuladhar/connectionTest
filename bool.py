string = "This is a string" #string

list1 = [1,2,3,4,5] #list

list2 = ["Apple","Ball","Cat",1,2,3.14] #lists are immutable

tuple1 = (1,"two",3,"Four") #tuples are immutable


#APPEND(VALUE) TO ADD POP(INDEX) TO REMOVE

#list1.append(11)
#addlist.pop(6)

addlist=list1+list2

booltype1=True
booltype2=False


dictionary ={"num1": 456,
            "num2":387 }
#print(dictionary["num1"])

dictionary["new_num"]=256

set1={34,45,56}
set2={34,45,56,34}

set2.add(90)
#print(set2)

#list() creates empty list
#list.insert(index,entry)

#INDEXING 
#first=addList[0]
#last=addlist[-1]

#NESTED LIST and indexing

multiList=[["index0FirstElement","index1FirstElement"],["index0SecondElement"]]

#print(multiList[1][0])

#List Slicing

list3=[i for i in range(10)]
print(list3[1:5])
print(list3[5:])

#DICTIONARY DETAILS
#print(dict1.keys())
#print(dict1.values())
#dict1.items()#outputs valies as tuples
#print(length(dict1))

