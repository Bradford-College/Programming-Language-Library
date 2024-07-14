'''
Functions in Python
Keyword: def
General format: def function_name(args)

A function in Python consists of:
- A function name: The identifier used to call the function.
- A set of operations: The block of code that performs specific tasks.
- A return value (optional): The value that the function outputs after execution.

Functions promote code reuse and maintainability by allowing you to define a block of code once and reuse it multiple times.
'''
# country = 'Nigeria'
# print('Hello World: ', country)

'''
 Inbuilt functions - e.g print(), len(), str(), int(), for 
 user defined functions
'''

'''
Variable Scope
    - local : declared in functions or classes and are not accessible outside of them except it is returned as a value 
    - global: declared outside functions, classes and loops 
'''

def listItems(fruits):
    for fruit in fruits:
        print(fruit)

listItems(fruits=['Apple','Grapes','Pear'])
fruits = ['Grapes', 'Oranges', 'Kiwi']
listItems(fruits)

print(len(fruits))