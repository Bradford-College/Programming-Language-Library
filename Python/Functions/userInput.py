'''
    working with user input
    keyword: input()
    general form : var_name = input(prompt)
    usage: allows input from the user console
'''

name = input("What is your name? ")

def helloName(name):
    '''
        desc: takes a name(str) and returns it with Hello
        args: name(str)
        return: none 
    '''
    
    print(f"Hello, {name}")

'''
Functions would not run until they are called.
'''
helloName(name)