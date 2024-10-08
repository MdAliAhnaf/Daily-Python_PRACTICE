print("Hello, World!")

print("""Print
Multiple
Lines
""")
print(end = '\n')


#print techniques <<String Formatting>>
#print('Pluto's a planet!')  # a single quote character inside a single-quoted string, Python gets confused
print('Pluto\'s a planet!')  # fix this by "escaping" the single quote with a backslash

another_pun = "The first time I got a universal remote control, I thought to myself \"This changes everything\"."
print(another_pun)
print(end = '\n')

new_line = "The first time I got a universal remote control, I thought to myself \n \"This changes everything\"."
print(new_line)
print(end = '\n')

planet = 'Pluto'
print([char+'! ' for char in planet])

claim = "Pluto is a planet!"
word = claim.split()
print(claim.index('plan')) # Searching for the first index of a substring
print(claim.split()) #split() method splits a string into a list
print(end = '\n')

#Combine a list of strings with an empty string delimitor (computer code that separates words)

list_of_string = ["ab", "cd", "ef"]
print("".join(list_of_string))
print(" ".join(list_of_string))

print(end = '\n')

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print (year)
print('/'.join([month, day, year]))

print('👏' .join([x for x in claim]))
print(' 👏 '.join([i.upper() for i in claim])) # # Yes, we can put unicode characters right in our string literals :)
print(' 👏 '.join([i.upper() for i in word]))

print(end = '\n')

print(ord("a")) #ASCII value

print(end = '\n')

astring = "Hello world!"
print(astring.index("o")) #returns first occurrence index number & this method only recognizes the first one
print(astring.count("l"))
print(astring[3:7]) 
print(astring[10])
print(astring[:-1]) #except last one all the others
print(astring[-1]) #selecting last one
print(astring[::2]) # selecting in two steps from the forward of a string
print(astring[::-2]) #reverse a string & selecting them in two steps
print(astring[::-1]) #reverse a string
print(astring.upper())
print(astring.lower())
print(astring.capitalize()) # changes first character to uppercase

today = 'Saturday'
another_day = today.replace("Satur", "Wednes")
print(another_day)

print(astring.startswith("Hello")) #checks true or false if the matching string start with that particular 
print(astring.endswith("asdfasdfasdf")) #checks true or false if the matching string ends with that particular 

#split() method splits a string into a list
afewwords = astring.split(" ") #splits at a space, the first item in the list will be "Hello", and the second will be "world!". 
print(afewwords)
print(end = '\n')

print("Sun,Mon,Tue,Wed,Thu,Fri,Sat".split(","))

a_long_line = "       This is a long line with some space before, after,     and some space in the middle..    "
a_long_line_stripped = a_long_line.strip() #removes whitespace characters from the beginning and end of a string.
print(a_long_line_stripped)


s , f, i = "string" , 10.00, 20
if s == "string":
    print("printing: %s")
    print("printing: %s" %s)



mystring, myfloat, myint = "hello" , 10.0, 20
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0: #Return whether an object is an instance of a class or of a subclass thereof. A tuple, as in isinstance(x, (A, B, ...))
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)



print(end = '\n')

zip_code= 12345
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    print("Zip code has 5 no of digits: %d" %zip_code)
    return (len(zip_code) == 5 and zip_code.isdigit())
is_valid_zip(zip_code)



def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code"""
    zip_code_str = str(zip_code)
    print("Zip code has 5 digits: %s" % zip_code_str)
    return len(zip_code_str) == 5 and zip_code_str.isdigit()

zip_code = 12345
print(is_valid_zip(zip_code))



lotsofhellos = "hello" * 10 #print 10 times
print(lotsofhellos) 
print(end = '\n')

a=5
print(f'a is {a}') # Preferred method for cvpr.
print('a is {}'.format(a))
print('a is ' + str(a))
print('a is %d %d' % (a, a))
print(end = '\n')

print(1, 2, 3, sep=' < ')
#boolean
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints False "is" operator does not match the values of the variables, but the instances themselves

t = True
f = False
print(type(t)) # Prints "<class 'bool'>"
print(not t)   # Logical NOT; prints "False"
print(t != f)  # Logical XOR; prints "True"
print(end = '\n')

#Arithmetic - operations
print(5 / 2) # float
print(5 // 2) # // operator -> rounded down to the next integer
#Exponentiation ``a`` raised to the power of ``b
a, b = 2 , 3
print (a ** b)
print(end = '\n')

#Built-in Functions
# min and max return the minimum and maximum of their arguments, respectively...
print(min(1, 2, 3))
print(max(1, 2, 3))

# abs returns the absolute value of an argument
print(abs(32.5))
print(abs(-32))


#function practice
def round_to_two_places(num):
    return(round(num, 2))

print(round_to_two_places(3.14159))

def wants_plain_hotdog(ketchup, mustard, onion): #no toppings
    #return (ketchup or mustard or onion)
    return not (ketchup or mustard or onion)
print(wants_plain_hotdog(True,True,True))

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (ketchup + mustard + onion) == 1

def to_smash(total_candies, number_of_friends=3):
    # Return the number of leftover candies that must be smashed after distributing the given number of candies evenly between 3 friends.
    return total_candies % number_of_friends

total_candies = int(input("Enter the total number of candies: "))
print(to_smash(total_candies))


def cube(num): 
    return (num*num*num)

x = cube(3)
y = int(input("Input the number to be added with 27: "))
def add():
    z = x + y
    return (z)   
    
print(add())
print(end = '\n')

#do not know how many arguments that will be passed into function
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
print(end = '\n')
# number of keyword arguments is unknown which will be passed into function add two asterisk: ** before the parameter name
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
print(end = '\n')

#If we call the function without argument, it uses the default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function() #"Norway"
my_function("Brazil")
print(end = '\n')

#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
print(end = '\n')

#Python also accepts function recursion, which means a defined function can call itself.
#This has the benefit of meaning that you can loop through data to reach a result.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1) #for k value 6, 6 + tri_recursion(k - 1) it calls tri_recursion(5) recursively/repeadetly (6-1); 5+4+3+2+1+0 stored in result and added with k=6 as total value of 21
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
print(end = '\n')

# string.strip(characters)
#The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) 
#characters (space is the default leading character to remove)

#if-else hacker-rank
n = int(input().strip())
#n = int(input("Enter an integer number: ").strip())
#print ("type of number", type(n))
#print ("Inserted number is: " + n)
if 1<=n<=100:  
    if n%2==0 and n>20:
        print("Not Weird")
    elif n%2==0 and 2<=n<=5:
        print("Not Weird")
    elif n%2!=0: 
        print("Weird")
    if n%2==0 and 6<=n<=20:
        print("Weird")
else: 
    print("Out of the range of 1 to 100")
print(end = '\n')

#arithmetic operators hacker-rank
a = int(input())
b = int(input())

if 1<=a<=10 ** 10 and 1<=b<=10 ** 10:  
    
        print(a+b)
        print(a-b)
        print(a*b)
    
else: 
    print("Out of the range of 1 to 10**10")
print(end = '\n')

#python division hacker-rank
a = int(input())
b = int(input())

print (int(a/b))
print(float(a/b)) 
print(end = '\n')

the_3_mus = ('Athos', 'Porthos', 'Aramis')
a_candidate = "D'Artagnan"

if a_candidate in the_3_mus:
    print ("%s is a musketeer" %a_candidate)
else:
    print ("%s is not a musketeer" %a_candidate)

print(end = '\n')

#python loops hacker-rank
n = int(input().strip())
if 1<=n<=20:
    for i in range(0, n):
            print(i ** 2)    
else: 
    print("Out of the range of 1 to 20")
print(end = '\n')

#python function hacker-rank
def is_leap(year):
    leap = False   
    if 1900<=year<=(10**5):  
        if year%400==0 and year%100==0: #The year can be evenly divided by 100 if its also divisible by 400
            leap = True
        elif year%4==0 and year%100!=0: #The year can be evenly divided by 4 hence not with 100 
            leap = True
        else:
            return False
        return leap
    else: 
        print("Out of the range of year 1900 to 10**5")
  
year = int(input().strip())
print(is_leap(year))
print(end = '\n')


def is_leap(year):
     leap = False
     if year%4==0:
          leap = True
          if year%100==0:
               leap = False
               if year%100==0 and year%400==0:
                    leap = True
     else:
          return False
     return leap
        
year = int(input())
print(is_leap(year))

#python function hacker-rank 123...n
# By default Python‘s print() function ends with a newline
# By default, the value of this parameter is ‘\n’ set end = '\n'

n = int(input().strip())
if 1<=n<=150:
    for i in range(1, (n+1)):
            
            print(i, end = '')
            #print(i, end = '\n')  
            #print(i, end = '@no-new_line-concate')    
else: 
    print("Out of the range of 1 to 20")
print(end = '\n')

#python math
import math
AB = float(input().strip())
BC = float(input().strip())

if 0<AB<=100 and 0<BC<=100:
    x = math.degrees(math.atan(AB/BC)) #inverse of tan (opposite/base)
    #print(int(x) , chr(176), sep= '')
    print(f'{round(x)}{chr(176)}') #character that represents the unicode 176 as (angle/degree)
else: 
    print("Out of the range of 1 to 100")
print(end = '\n')


print ( ((2 + 5) * (1+1)) / (2+2) )


