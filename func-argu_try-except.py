nums = [1, 2, 3, 3]

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for x in nums:  # loop iterates over each element, nums = [1, 2, 3, 3]
            if x in hashset:  # does this element exist in the hashset
                return True
            # print(x) #prints nums each elements
            hashset.add(x)  # adding each elements to set(set doesn't allows duplicates)
        return False

# Create an instance of the Solution class
solution = Solution()
# Call the containsDuplicate method and print the result
result = solution.containsDuplicate(nums)
print(result)  # This should print True because there is a duplicate (3) in the list


def dupli(nums):
    
    hashset = set()
    for x in nums:
        if x in hashset:
            return True
        hashset.add(x)
    return False

result = dupli([1, 2, 3, 3])

print(result)


print(end = "\n")


import math

def loan_emi(amount, duration, rate, down_payment=0):
    loan_amount = amount - down_payment
    emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    emi = math.ceil(emi)
    return emi


emi1 = loan_emi(
    amount=1260000, 
    duration=8*12, 
    rate=0.1/12, 
    down_payment=3e5
)

print(emi1)

print(end = "\n")

import math

def loan_emi(amount, duration, rate, down_payment=0):
    try:
        loan_amount = amount - down_payment
        if loan_amount <= 0:
            raise ValueError("The loan amount must be greater than zero after down payment.")

        emi = loan_amount * rate * ((1 + rate) ** duration) / (((1 + rate) ** duration) - 1)
        emi = math.ceil(emi)
        return emi
    #Several except blocks handle different types of exceptions
    except ZeroDivisionError:
        print("Error: Division by zero occurred. Check the rate and duration values.")
        return None
    except TypeError:
        print("Error: Invalid input type. Please ensure all inputs are numbers.")
        return None
    except ValueError as ve:
        print(f"Value Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

try:
    emi1 = loan_emi(
        amount=1260000, 
        duration=8*12, 
        rate=0.1/12, 
        down_payment=3e5
    )
    print(emi1)
except Exception as e:
    print(f"An error occurred while calculating EMI: {e}")

print(end = "\n")


try:
    print("Now computing the result..")
    #When an exception occurs inside a try block, the block's remaining statements are skipped
    result = 5 / 0
    print("Computation was completed successfully")
#The except block is executed if the type of exception thrown matches that of the exception being handled.
except ZeroDivisionError: #error type matches
    print("Failed to compute result because you were trying to divide by zero")
    result = None

print(result)





    



