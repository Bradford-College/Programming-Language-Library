'''
    Python lists 
    list items/elements are accessed by index number
    array indexing starts at 0
    the last element in an array/list is the len(arr) - 1
'''

cars = ['Toyota', 'Mini-cooper', 'BMW'] #array

number_of_cars = len(cars)

print("The number of cars is :", number_of_cars)

'''
    accessing elemenets in an array by index
'''
print(cars[2]) # prints BMW
print(cars[0]) # prints Toyota

'''
    index() 
    it returns the index location of a variable 
'''
print("The index of BMW is, ", cars.index("BMW"))

'''
    append()
    inserts a value to the array 
'''
cars.append("Tesla")
print(cars)

'''
    remove()
    removes specified value
'''
cars.remove("Tesla")
print(cars)