'''
Exception Handling in Python
Keyword: try-except
General format: try:
                    # Block of code to attempt
                except ExceptionType as e:
                    # Block of code to handle exceptions of type ExceptionType

Exception handling in Python allows you to gracefully manage and recover from errors that may occur during program execution.
The try block contains the code that may throw an exception, while the except block handles the exception if it occurs.

Types of errors and exceptions include:
- SyntaxError: Occurs when the syntax of the code is incorrect.
- NameError: Raised when a local or global name is not found.
- TypeError: Raised when an operation or function is applied to an object of inappropriate type.
- ValueError: Raised when a function receives an argument of the right type but inappropriate value.
- IndexError: Raised when trying to access an element from a list using an index which is out of its range.
- KeyError: Raised when a dictionary key is not found.
- IOError: Raised when an input/output operation fails.
- ZeroDivisionError: Raised when division or modulo operation is performed with zero as the denominator.

This approach promotes robustness in your code by preventing crashes and allowing you to implement alternative behaviors 
or error messages based on the type of exception encountered.
'''


'''
Function to prompt user 
'''

def prompt():
    x, y = 0,0 # initialize the variable 
    while True:
        try:
            x = int(input("Enter First number: "))
            y = int(input("Enter Second number: "))
            break
        except ValueError:
            print("Invalid Data type received", ValueError)
    return x,y

# Cal function 
x, y = prompt()

'''
 Function to show zerodiviison error 
'''
def divideTwo(x, y):
    while True:
        try:
            output = x/y
            print(output)
            break
        except ZeroDivisionError:
            print("Can not divide by zero", ZeroDivisionError)

# call divideTwo() function
divideTwo(x, y)

''' 
    Update the calculator app, to include try... except... finally statements 
'''