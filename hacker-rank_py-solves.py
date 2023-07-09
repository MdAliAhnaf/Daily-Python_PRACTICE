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

#python math Triangle Quest 2