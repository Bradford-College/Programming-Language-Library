'''
    If statements:
    edge
    Example:
    Largest Between Two Numbers
'''

a = 40
b = 40

if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} equals {b}")
else:
    print(f"{b} is greater than {a}")
'''
 List, using if statements in list 
 Half-ifs
'''

names = ['Dilan', 'Mark', 'David', 'Ali']
# Check if a name exists in list

name = 'Ali'
if name in names:
    print(f"found {name}")