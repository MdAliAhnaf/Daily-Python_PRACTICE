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
print(list(filter(lambda a: a>3, nums)))
print(list(map(lambda a: a>3, nums)))
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