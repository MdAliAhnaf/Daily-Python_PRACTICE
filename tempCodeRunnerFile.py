c_tupl = ("apple", "banana", "cherry")
temp = [*c_tupl,]#convert the tuple into a list
temp[1] = "kiwi" #change the list at index
temp.insert(4, "orange")
c_tupl = tuple(temp) #convert the list back into a tuple
print(c_tupl)
print(end = '\n')