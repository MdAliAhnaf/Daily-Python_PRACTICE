word= "Hi Noob"
print(word)

splitter= word.split()

print(splitter)

print("".join(splitter))
print(" ".join(splitter))
print("WEW".join(x for x in splitter))
print("WEW".join(x for x in word))

print(word[::2])


n = int(input())
if 1<=n<=150:
    for x in range(1,n+1):
            print(x,end = '')
else:
    print("sleep")
    
#with function
def print_n(n):
    if 1 <= n <= 150:
        for x in range(1, n + 1):
            print(x, end='')  
    return

n = int(input())
print_n(n)

for x in range (6,-6,-1):
     print(x)


arr = [1,2,3,4,5]

arr.append(4)

print(arr)



def dupli(nums):
     
     hashset = set()

     for x in nums:
        if x in hashset:
            return True

        hashset.add(x)
          
     return False

nums = [1, 2, 3, 4]

print(dupli(nums))


def dupli(nums):
    lent = len(nums)
    for i in range(lent):
        for j in range(i+1, lent):
            if nums[i] == nums[j]:
                return True
    return False

nums = [1, 2, 3, 3]

print(dupli(nums))


def sum_n(arr):
    result = []
    lent = len(arr)
    
    for i in range(lent):
        for j in range(i + 1, lent):
            if arr[i] + arr[j] == max_sum_value:
                result.append((arr[i], arr[j]))  # Store the pair
    return result

max_sum_value = 5

arr = [1, 2, 3, 4, 5]
pairs = sum_n(arr)
print(pairs)


