from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]
def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers) #reduce takes the first and second elements in numbers and passes them to custom_sum respectively
                                     #custom_sum computes their sum and returns it to reduce
#use the optional initial value
result_ini = reduce(custom_sum, numbers, 20)
print(result)
print(result_ini) #initially, uses 10 as the first argument to custom_sum

l = [ 1, 10, 20, 3, -2, 0]
result = reduce(lambda x,y: x+y,l)
print(result)