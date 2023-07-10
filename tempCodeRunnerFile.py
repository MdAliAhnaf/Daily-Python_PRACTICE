car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car, type(car))
print("Paired key's value of the key BRAND: " + car["brand"]) #prints key's value as pairs
print(end = '\n')
x = car.keys()
y = car.values()
print(x) #before the change
print(y)

car["color"] = "white"
car["color"] = "black"
car["year"] = "2022"
print(x) #after the change
print(y)
print(end = '\n')

#The setdefault() method returns the value of the item with the specified key.
#setdefault() works when key is in the dictionary
df = car.setdefault("color", "white")
print(df)
print(end = '\n')
# If the key does not exist, insert the key, with the specified value <<default_value is provided>>
df_not_exists = car.setdefault("tyre", "CEAT")
print(df_not_exists)