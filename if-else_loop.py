
a_number = 9

if a_number % 2 == 0:
    pass #if statements cannot be empty; pass statement to do nothing and avoid getting an error
elif a_number % 3 == 0:
    print('{} is divisible by 3 but not divisible by 2'.format(a_number))


print(end = '\n')

print("INCREMENTED FOR LOOP") 
for x in range(0, 5, 2): 
    print(x) 
  
# this is for increment operator here start = 5, 
# stop = -1 and step = -1 
print("\n DECREMENTED FOR LOOP") 
for i in range(6, -4, -2): 
    print(i) 
    

print(end = '\n')

def print_n(n):
  
    if 1<=n<=150:
        for x in range(1,n+1):
            print(x,end = '')
    return

n = int(input())




result = 1
i=1

while i<=4:

    #result = result * i 
    #i = i + 1

    result *= i
    
    # if i == 4:
    #     print('Loop upto fac 4 reached! Stopping execution..')
    #     break
    
    i += 1

print('The factorial of 4 is: {}'.format(result))

print(end = '\n')

#Multiply odds only
result = 1

while i < 10:
    i += 1
    if i % 2 == 0:
        print('Skipping {}'.format(i))
        continue #not end the loop entirely, but simply skip the remaining statements in the loop and continue to the next loop
    print('Multiplying with {}'.format(i))
    result = result * i
    
print('i:', i)
print('result:', result)

print(end = '\n')

#opposite diff way coding factorial
result = 4
i = 3

while i >= 1:
    result *= i
    i -= 1

print('The factorial of 4 is: {}'.format(result))


star = '*'
m_length = 10

while len(star) < m_length:
    print(star)
    star += '*'

while len(star) > 0:
    print(star)
    star = star[:-1]


print(end = '\n')

# star = '*'
# m_length = 10

# for i in range(1,m_length):
#     print(star)
#     star += '*'

# for i in range(m_length,0,-1):
#     print(star)
#     star = star[:-1]


# Define the maximum length of the pattern
max_length = 6

# Print the increasing pattern
i = 1
while i <= max_length:
    print(' ' * (max_length - i) + '*' * i)
    i += 1

# Print the decreasing pattern
i = max_length - 1
while i > 0:
    print(' ' * (max_length - i) + '*' * i)
    i -= 1



# # Define the maximum length of the pattern
# max_length = 6

# # Print the increasing pattern
# i = 1
# for i in range(1,max_length+1):
#     print(' ' * (max_length - i) + '*' * i)
#     i += 1

# i = max_length - 1
# for i in range(i,0,-1):
#     print(' ' * (max_length - i) + '*' * i)
#     i -= 1
print(end = '\n')

max_length = 6

# Print the increasing pattern
i = 1
while i <= max_length:
    print(' ' * (max_length - i) + '*' * (2 * i - 1))
    i += 1

# Print the decreasing pattern
i = max_length - 1
while i > 0:
    print(' ' * (max_length - i) + '*' * (2 * i - 1))
    i -= 1

print(end = "\n")

nums = [1,2,3]

for i,n in enumerate(nums):
    print(i,n)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# for x in range(len(days)):
for x in days:
    print(x)

obj1 = enumerate(days)

print(obj1)
print(type(obj1))

print(list(enumerate(days)))

print(end = "\n")

#Ranges are used for iterating over lists to track the index of elements while iterating.
for x in range(len(days)):
    print('The value at position {} is {}.'.format(x, days[x]))

#enumerate function with a list as an input, which returns a tuple containing the index (x) and the corresponding element (y)
for x, y in enumerate(days):
    print('The value at position {} is {}.'.format(x, y))

fruit = ('Apple', 'Banana', 'Guava')

for x in fruit:
    print(x)

person = {
    'name': 'John Doe',
    'sex': 'Male',
    'age': 32,
    'married': True
}

# for x in person:
#     print(x, person[x])

for key in person:
    print(key, person[key]) #person[key] to access pair value's

print(end = "\n")

#iterate directly over the values using the .values method

for value in person.values():
    print(value)
    
print(end = "\n")

#iterate directly over the over key-value pairs using the .items method.
for key_value_pair in person.items():
    print(key_value_pair)

print(end = "\n")

for key,value in person.items():
    print(key,value)

persons = [{'name': 'John', 'sex': 'Male'}, {'name': 'Jane', 'sex': 'Female'}]


for x in persons:
    for key in x:
        print(key,x)






for x in persons:
    for key in x:
        print(key, ":", x[key])
    print(" ")