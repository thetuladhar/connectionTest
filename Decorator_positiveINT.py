def positive_decorator(function):
  def wrapper():
    #print("\nMessage BEFORE the function execution")
    number=function()
    #print("Message AFTER the function execution")
    
    #check if number is positive or negative
    if number > 0:
      print("Number is a positive number")
    elif number <0:
      print("Number is a negative number")
    
    #some error handlers
    elif number==0:
      print("Zero is a neutral number")
    else:
        print("Something went wrong. Please input a number.")

  return wrapper


@positive_decorator
def take_number():
  #get input from user
  num=int(input("Enter a number : "))
  #return the number
  return num
  
take_number()
take_number()
take_number()