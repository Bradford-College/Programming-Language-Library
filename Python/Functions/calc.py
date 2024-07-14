'''
Interractive Calculator 

'''

def promptUser():
    # Prompt user
    num_1 = input("Enter First Number: ")
    num_2= input("Enter Second Number: ")

    # cast variable to int
    a = int(num_1)
    b = int(num_2)

    # print(f"the datatype of num_1 is {type(num_1)}, the dtype of a is {type(a)}")
    # print(f"the datatype of num_1 is {type(num_2)}, the dtype of a is {type(b)}")
    '''
        Guide User
    '''

    print("What type of oepration would you like to perform \n:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multuplication")
    print("/ for division")

    op = input("Enter type of operation: ")
    
    return a, b, op

''''
define a function that performs basic arithmetic operations 
float dtye : 0.1 ... 0.000 decimal numbers 
'''

def calculator(a:int, b:int, op:str) ->float:
    '''
        description : performs arithmetic operation on integrers
        args: 
            - a:int, 
            - b:int
            - op: str
        returns: int 
    '''
    output = 0 #initilazation 
    
    if op == '+':
        output = a + b
    elif op == '-':
        output = a - b
    elif op == '*':
        output = a * b
    elif op == '/':
        # nested if statement  
        if b!=0:
            output = a / b
        else:
            print(ZeroDivisionError)
    else:
        print("Invalid Operator entered")
    
    return output

# call promptuser()
a, b, op = promptUser()

#call function 
print(calculator(a, b, op))
