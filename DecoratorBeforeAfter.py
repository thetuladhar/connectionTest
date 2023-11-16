def hello_decorator(func):
    def wrapper():
        print("\nMessage Before Function Execution")
        func()
        print("Message After the Execution")
    return wrapper

@hello_decorator
def function_with_decorator():
    print("This is message inside the function using a decorator")

@hello_decorator
def test_error_message():
    print("This is an example of and error message")


function_with_decorator()
test_error_message()


