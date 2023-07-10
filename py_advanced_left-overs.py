#<<<<< Other Advanced -- python topics >>>>>

#The zip() function returns a zip object, which is an iterator of tuples
#the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together
a = [1,2,3,4,5]
b = [5,4,3,2,1]
print(zip(a,b))
print(list(zip(a,b)))
#If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
a = [1,2,3,4,5]
b = [7,6,5,4,3,2,1]
print(zip(a,b))
print(list(zip(a,b))) # prints [(1, 7), (2, 6), (3, 5), (4, 4), (5, 3)]