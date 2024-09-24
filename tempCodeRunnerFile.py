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