# <<LIST>>
#items are stored sequentially
#Lists are mutable
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
#in many ways, it is simillar to a list; one of the most important difference is that tuples can be used as KEYs in a dictionary or elements of a SET.

tupl = ('morning!', 'night' , 99 , 100)
for i in tupl:
    print(i)
print(end = '\n')
print(tupl[-1])

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%d"

print(format_string % data)

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

"CS" in depts

depts.remove("ARCHI")
print(depts)

"ARCHI" in depts