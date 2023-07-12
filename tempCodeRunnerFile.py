x = 0.125
print(x.as_integer_ratio())
#These multiple return values can be individually assigned as follows
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)