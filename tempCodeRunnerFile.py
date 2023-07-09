astring = "Hello world!"
print(astring.index("o")) #returns first occurrence index number & this method only recognizes the first one
print(astring.count("l"))
print(astring[3:7]) 
print(astring[10])
print(astring[-1])
print(astring[::-1]) #reverse a string
print(astring.upper())
print(astring.lower())

print(astring.startswith("Hello")) #checks true or false if the matching string start with that particular 
print(astring.endswith("asdfasdfasdf")) #checks true or false if the matching string ends with that particular 

afewwords = astring.split(" ")
print(afewwords)