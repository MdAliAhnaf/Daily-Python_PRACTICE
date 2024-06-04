try:
    print("Now computing the result..")
    result = 5 / 0
    print("Computation was completed successfully")
except ZeroDivisionError:
    print("Failed to compute result because you were trying to divide by zero")
    result = None

print(result)