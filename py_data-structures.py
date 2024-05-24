                                          # <<<<<<<<<< Data-Structures / Collections >>>>>>>>>>

# <<LIST>>
#items are stored sequentially
#Lists are mutable
#allows duplicates
#can hold on to different data types
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(sorted(planets))
print(end = '\n')

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

print(1 in a)

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3,2,0,2]
# d. The expression is the same as the list [2, 3], which has length 2.


list = ['hi' , 'bye' , 0, 9, 1, 2]
print(list)
print(list[2], list[1], list[-3]) #0, 1, 2, .... n [index] [-n] -> -1, - 2, .... -n (counting from backwards)

print(end = '\n')

#<<String Formatting>>
mylist = [1,2,3]
print("My list: %s" % mylist)

print(end = '\n')


fruits = ['apple', 'banana', 'cherry']
a_list = [23, 'hello', None, 3.14, fruits, 3 <= 5]
print(a_list)
print(end = '\n')
print(a_list[2:100])
print(a_list[12:10]) #empty list
print(end = '\n')
print(a_list[2:])
print(a_list[:5])

print(a_list[2:] or a_list[:5])

print(end = '\n')

print(a_list[-2:-5])
print(a_list[-5:-2])
print(a_list[-2:-5] or a_list[-5:-2])

print([1,2,3] * 3) #print the list's elements 3 times

for i,v in enumerate(list):
    print(f"{i}:{v}")

print(end = '\n')

c = []
c.append('a')
c.append('b')
c.append('c')
print(c)

c.insert(0, 'a0') #insert at index
print(c)

c.remove('b') #Remove element
print(c)

del c[0]  #Remove at index
print(c)

print(end = '\n')

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    temp = racers[0]
    racers[0] =  racers[-1]
    racers[-1] = temp
  
print(end = '\n')

x = object()
y = object()

x_list = [x] * 10 # contain 10 instances 
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# contain 10 instances 
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("x_list and y_list contains 10 objects")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great! big_list contains total 20 objects")

print(end = '\n')

listOfLists = [
    ['a','b','c'],
    ['One','Two']
]
print(listOfLists)

print(end = '\n')
# party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'] . 
# A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. 
# Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1


#<< List Comprehension >>
#offers a shorter syntax when you want to create a new list based on the values of an existing list in a single, readable line.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)
                                                                         # avoid doing this !!!!
                                                                            # <<< Instead >>>
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
upper_newlist = [x.upper() for x in fruits]
new_list = [x for x in range(120) if x%2 == 0]
print(newlist)
print(upper_newlist)
print(new_list)
print(end = '\n')


arr1 = [0,1,2,3,4,5,6,7,8,9]
arr1_copy= arr1.copy()
print(arr1_copy)

print(arr1_copy.pop()) #pops the last element here 9

arr1_copy.pop() #removes 8

print(arr1_copy) #0 to 7

print(end = '\n')

arr1_copy_newlist = [i for i in arr1]
print(arr1_copy_newlist)

sq = [i**2 for i in arr1]
print(sq)

sq_even = [i**2 for i in arr1 if i%2 == 0]
print(sq_even)
print(end = '\n')

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    return any([num % 7 == 0 for num in nums]) #The any() function returns True if any item in an iterable are true, otherwise it returns False

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numbers = [i for i in numbers if i>0]
print(positive_numbers)   
print(end = '\n')

# list comprehension on dictionaries
dictio = {(a,a): (a,a**2) for a in range(10) if a%2 == 0}
print(dictio)

print(end = '\n')

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    return any(meals[i] == meals[i+1] for i in range(len(meals)-1)) #The any() function returns True if any item in an iterable are true, otherwise it returns False

                                
# <<TUPLE>>
#ordered list of values
#immutable
#allows duplicates
#in many ways, it is simillar to a list; one of the most important difference is that tuples can be used as KEYs in a dictionary or elements of a SET.
#tuple() constructor to make a set
tupl = ('morning!', 'night' , 99 , 100)
for i in tupl:
    print(i)
print(end = '\n')
print(tupl[-1])

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%d"

print(format_string % data)
print(end = '\n')

#tuple() constructor to make a set
new_tupl = tuple(('hi' , 'bye' , 9, 11, 110))
print(new_tupl)
print(new_tupl[-1])
print(new_tupl[2:3]) # slicing operator
print(new_tupl[0:])
print(new_tupl[:4])
print(end = '\n')

c_tupl = ("apple", "banana", "cherry")
#temp = list(c_tupl) # convert the tuple into a list
# Using * unpacking method
temp = [*c_tupl,] # convert the tuple into a list
temp[1] = "kiwi" # change the list at index
temp.insert(4, "orange")
c_tupl = tuple(temp) #convert the list back into a tuple
print(c_tupl)
print(end = '\n')

fruits = ("apple", "banana", "Jack Fruit") #Packing a tuple
(red, yellow, green) = fruits #Unpacking a tuple

print(red)
print(yellow)
print(green)
print(end = '\n')

fruits_star = ("apple", "banana", "cherry", "strawberry", "raspberry") #Packing a tuple
(green, yellow, *red) = fruits_star #adding an * to the variable name and the values will be assigned to the variable as a list

print(green)
print(yellow)
print(red)
print(end = '\n')

fruits_d = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits_d #dynamically assigning

print(green)
print(tropic)
print(red)
print(end = '\n')

#normal check
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
print(end = '\n')  

tuple_add = thistuple + fruits_d
print(tuple_add)
count_apple = ("Number of apples: %d" % (tuple_add.count("apple")))
print(count_apple,"Index number of pineapple:", tuple_add.index("pineapple"))
print(end = '\n')  

#Tuples are often used for functions that have multiple return values.
#For example, the as_integer_ratio() method of float objects returns a numerator and a denominator in the form of a tuple
x = 0.125
print(x.as_integer_ratio())
#These multiple return values can be individually assigned as follows
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

# <<SETS>>
#Set holds an unordered collection of objects
#do not allow duplicates
#If a program adds a duplicate item to a set, only one copy of each item remains in the collection.
#Adding a duplicate item to a set does not result in an error. 
#dynamically add items to a set with the add function

depts = {"MBA","EEE","BBA","ARCHI"}
print(depts, type(depts))

depts.add("CS")
print(depts)
print("CS" in depts)
#If the item to remove does not exist, remove() will raise an error.
depts.remove("ARCHI")
#If the item to remove does not exist, discard() will NOT raise an error. if exists it removes
depts.discard("lol")

# "ARCHI" in depts #in jupyter notebook prints the last cell
def detect_rem():
    if "ARCHI"  in depts:
      return True  
    else:
        return False
print(detect_rem())

print(end = '\n')
print(depts)

thisset = {"apple", "cherry", True, 1, 2} # True and 1 are same <<no-duplicates>>
print(thisset, "length:" ,len(thisset), (type(thisset)))

#set() constructor to make a set
new_set = set(('hi' , 'bye' , 0, 9, 1, 2))
print(new_set , (type(new_set)))
print(end = '\n')

#update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
add_tuple_update = tuple(("Jack Fruit" , "Mango"))
thisset.update(mylist)
thisset.update(add_tuple_update)
print(thisset)

#pop() method to remove an item, but this method will remove a random item
thisset.pop()
print(thisset)

#clear() method empties the set <<blank set with no value>> but the set remains there
thisset.clear()
print(thisset)

#del keyword will delete the set completely <<shows error>>
del thisset
print(end = '\n')

print(set("Eric"))
#cosidering a is set 1 and b is set 2
a = set(["Jake", "John", "Eric"]) #converting list to set
print(a)
#same
print(set("Eric".split())) #split() method splits a string into a list
print(end = '\n')

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b)) #takes the common
print(a.symmetric_difference(b))  #attended only one of the events / non-common
print(a.difference(b)) #members attended only one event and not the other
print(a.union(b)) #list of all participants 

# <<Dictionaries>>
# a collection of name-value pairs <store data values in key:value pairs>
# As of Python version 3.7, dictionaries are ordered #In Python 3.6 and earlier, dictionaries are unordered.
# a collection which is ordered*, changeable and do not allow duplicates
# data type similar to arrays, but works with keys and values instead of indexes

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car, type(car))
print("Paired key's value of the key BRAND: " + car["brand"]) #prints key's value as pairs
print(end = '\n')
x = car.keys()
y = car.values()
print(x) #before the change
print(y)

person1 = dict(name='Jane Judy', sex='Female', age=28, married=False)
print(person1)

person1['address'] = '1, Penny Lane'
print(person1)
person1.pop('address')
print(person1)
print(person1.keys())
print(person1.values())
print(person1.items())

print(person1.get("name"))
print(person1.get("address", "Unknown"))

car["color"] = "white"
car["color"] = "black"
car["year"] = "2022"
print(x) #after the change
print(y)
print(end = '\n')

#The setdefault() method returns the value of the item with the specified key.
#setdefault() works when key is in the dictionary
df = car.setdefault("color", "white")
print(df)
print(end = '\n')
# If the key does not exist, insert the key, with the specified value <<default_value is provided>>
df_not_exists = car.setdefault("tyre", "CEAT")
print(df_not_exists)


z = car.items() #complete dictionary items
print(z)
if "color" in car:
  print("Yes, 'color' is one of the keys in the car dictionary")
else:
   print("ERROR")
print(end = '\n')

car.update({"year": 2023})
print(car)
print(end = '\n')
# popitem() method removes the <<last inserted>> item (in versions before 3.7, a random item is removed instead)
car.popitem()
print(car)
del car["model"]
print(car)
car.clear() # clear() method empties the dictionary
print(car)
del car # del keyword can  delete the dictionary completely

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
x = thisdict.get("country")
print(x)

d = {'person': 2, 'cat': 4, 'dog': 4, 'spider': 8}
for i in d: 
    print(i) #keys 
print(end = '\n')
for i in d:
    y = d[i] #from keys takes paired values <<only values>>
    print('A %s has %d legs' % (i, y))
print(end = '\n')
for i,y in d.items():
    print('A %s has %d legs' % (i, y)) 
print(end = '\n')

#nested dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004,
  "height" : str(168) + ' in cm'
}
child2 = {
  "name" : "Tobias",
  "year" : 2007,
  "height" : str(100) + ' in cm'
}
child3 = {
  "name" : "Linus",
  "year" : 2011,
  "height" : str(130) + ' in cm'
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
print(myfamily["child1"])
print(end = '\n')
print(myfamily["child2"]["name"], myfamily["child2"]["year"])
print(end = '\n')

#The fromkeys() method creates a dictionary from the given sequence of keys and values.
# set of vowels # keys for the dictionary
keys = {'a', 'e', 'i', 'o', 'u' }
# assign string to the value # value for the dictionary
value = 'vowel'
# creates a dictionary with keys and values
vowels = dict.fromkeys(keys, value)
print(vowels)
print(end = '\n')

print(bool(False))
print(bool(0.0))
print(bool(None))

print(bool(True), bool(""), bool([1,2]), bool((2,3)), bool([]), bool({}), bool(set()), bool(range(0)), bool(range(10)))

none_var = None
print(type(none_var))