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
