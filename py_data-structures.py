# <<LIST>>
#items are stored sequentially
#Lists are mutable
#can hold on to different data types

list = ['hi' , 'bye' , 0, 9, 1, 2]

print(list)
print(list[2], list[1], list[-3]) #0, 1, 2, .... n [index] [-n] -> -1, - 2, .... -n (counting from backwards)

print(end = '\n')

for i,v in enumerate(list):
    print(f"{i}:{v}")

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

