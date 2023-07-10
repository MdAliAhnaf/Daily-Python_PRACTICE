fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
upper_newlist = [x.upper() for x in fruits]
new_list = [x for x in range(120) if x%2 == 0]
print(newlist)
print(upper_newlist)
print(new_list)
print(end = '\n')