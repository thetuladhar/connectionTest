import time
def runtime_decorator(function):
  def wrapper(n): #ADDED 'n'as argumemt because wanted to take input
    
    start = time.time()
    #print("\nMessage BEFORE the function execution")
    function(n)   
    #print("Message AFTER the function execution")
    end = time.time()
    #from 
    print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
  return wrapper

@runtime_decorator
def looper(n):#ADDED 'n'as argumemt because wanted to take input
  for i in range(n):
    return i

looper(10)

looper(9000)