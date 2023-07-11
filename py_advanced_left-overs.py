#<<<<< Other Advanced -- python topics >>>>>

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
#MAP
# map(func, *iterables)
# the asterisk(*) on iterables; It means there can be as many iterables as possible
# map() function executes a specified function for each item/element in an iterable. The item is sent to the function as a parameter.

def myfunc(a):
  return len(a) #returns the length of the strings

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
#convert the map into a list, for readability:
print(list(x))


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