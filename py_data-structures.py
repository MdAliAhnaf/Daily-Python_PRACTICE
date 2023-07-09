# <<LIST>>
#items are stored sequentially
#Lists are mutable
#allows duplicates
#can hold on to different data types

list = ['hi' , 'bye' , 0, 9, 1, 2]

print(list)
print(list[2], list[1], list[-3]) #0, 1, 2, .... n [index] [-n] -> -1, - 2, .... -n (counting from backwards)

print(end = '\n')

#<<String Formatting>>
mylist = [1,2,3]
print("My list: %s" % mylist)

print(end = '\n')

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
print(new_tupl[2:3])
print(new_tupl[0:])
print(new_tupl[:4])
print(end = '\n')

c_tuple = ("apple", "banana", "cherry")
temp = list(c_tuple) #convert the tuple into a list
temp[1] = "kiwi" #change the list at index
temp.insert(4, "orange")
c_tuple = tuple(temp) #convert the list back into a tuple
print(c_tuple)
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
print(thisset)

print(set("Eric"))

a = set(["Jake", "John", "Eric"]) #converting list to set
print(a)
#same
print(set("Eric".split())) #split() method splits a string into a list
print(end = '\n')

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b)) #takes the common
print(a.symmetric_difference(b))   #attended only one of the events / non-common