#<<<<< Other Advanced -- python topics >>>>>

#Python no longer has explicit pointers like C or C++, however, 
#it does utilize references, which are comparable concepts. Python serves everything as an object and variables serve as pointers to those objects.
a = 5
b = a
a = 6
print(b)

#The zip() function returns a zip object, which is an iterator of tuples
#the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together
a = [1,2,3,4,5]
b = [5,4,3,2,1]
print(zip(a,b))     #zip object at 0x........
print(list(zip(a,b)))
print(end = '\n')

for n1,n2 in zip(a,b):
   print(n1,n2)

print(end = '\n')
#If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
a = [1,2,3,4,5]
b = [7,6,5,4,3,2,1]
print(zip(a,b))     #zip object at 0x........
print(list(zip(a,b))) # prints [(1, 7), (2, 6), (3, 5), (4, 4), (5, 3)]
print(end = '\n')

# << MAP >>
# map(func, *iterables)
# the asterisk(*) on iterables; It means there can be as many iterables as possible
# map() function executes a specified function for each item/element in an iterable. The item is sent to the function as a parameter.

def myfunc(a):
  return len(a) #returns the length of the strings

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
#convert the map into a list, for readability:
print(list(x))
print(end = '\n')

def myfunc(a, b):
  return a + b  #adds strings

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)     #map object at 0x........
#convert the map into a list, for readability:
print(list(x))

print(end = '\n')

def addtion(x):
    return x+x

nums = [1,2,3,4,5,6]
res = map(addtion, nums)
print(list(res))
print(end = '\n')

def pre_process(str):
    t = str.strip()
    return t[0].upper()+t[1:]

l1 = ['   apple  ', 'pear ', ' orange', 'mango', 'pine apple  ']
print(list(map(pre_process, l1)))

l2 = [pre_process(x) for x in l1] #List Comprehension 
print(l2)
print(end = '\n')

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 4)))
print(result)
print(end = '\n')

# << FILTER >>
# filter(func, iterable)
# Unlike map(), only one iterable is required.
# The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to it.
# filter passes each element in the iterable through func and returns only the ones that evaluate to true.
def greater_than_five(x):
    return x>5

l = [ 1, 10, 20, 3, -2, 0]
l2 = list(filter(greater_than_five, l))
print(l2)
print(end = '\n')

# << Lambda >>
# a small anonymous function that can take any number of arguments, but can only have one expression
# instead of defining the function somewhere and calling it, lambda functions can be used, 
# which are inline functions defined at the same place we use it
# your_function_name = lambda inputs : output
# write less code (be "Pythonic")

nums = [ 1, 10, 20, 3, -2, 0]
print(list(map(lambda a: a+a, nums)))
print(list(filter(lambda a: a>3, nums))) #filters based on the condition
print(list(map(lambda a: a>3, nums))) #return Boolean based on the condition
print(end = '\n')
x = lambda a, b : a * b
print(x(5, 6))
print(end = '\n')

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results_zip = list(zip(my_strings, my_numbers))
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))  # (x, y) outputs as tuples
print(results_zip)
print(end = '\n')
print(results)

# << Reduce >>
# reduce(func, iterable[, initial])
# Like filter and map the reduce function also works on a list. However, the result of the reduce is a <<single value>>. 

from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers) #reduce takes the first and second elements in numbers and passes them to custom_sum respectively
                                     #custom_sum computes their sum and returns it to reduce
#use the optional initial value
result_ini = reduce(custom_sum, numbers, 20)
print(result)
print(result_ini) #initially, uses 10 as the first argument to custom_sum
print(end = '\n')
l = [ 1, 10, 20, 3, -2, 0]
result = reduce(lambda x,y: x+y,l)
print(result)
print(end = '\n')

# << Generators >>
# Generators are simple functions which return an iterable set of items, one at a time, in a special way.
# When an iteration over a set of item starts using the for statement, the generator is run
# Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set.
# The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.

import random
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    print(end = '\n')
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))

print(end = '\n')

# << Classes and Objects >>
# Python is an object oriented programming language
# Almost everything in Python is an object, with its properties and methods
# A Class is like an object constructor, or a "blueprint" for creating objects and essentially a template to create objects
# Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes.

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass() # "myobjectx" holds an object of the class "MyClass" that contains the variable and the function defined within the class called "MyClass".
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)
print(end = '\n')

# The __init__() function, is a special function that is called when the class is being initiated. 
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# It's used for assigning values to object properties, or other operations that are necessary to do when the object is being created in a class .
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# The string representation of an object WITHOUT the __str__() function

myobjectp1 = Person("John", 36)

print(myobjectp1.name)
print(myobjectp1.age)

print(end = '\n')
# The __str__() function controls what should be returned when the class object is represented as a string
# If the __str__() function is not set, the string representation of the object is returned

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):                     # The string representation of an object WITH the __str__() function
    return f"NAME: {self.name} AGE:({self.age})"

myobjectp1 = Person("John", 36)
print(myobjectp1)

print(end = '\n')

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)
print(x.bit_length())