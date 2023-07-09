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
print(x)

car["color"] = "white"
car["color"] = "black"
car["year"] = "2022"
print(x) #after the change
print(y)
print(end = '\n')


z = car.items()
print(z)
if "color" in car:
  print("Yes, 'color' is one of the keys in the car dictionary")
else:
   print("ERROR")
print(end = '\n')

car.update({"year": 2023})
print(car)
print(end = '\n')
# popitem() method removes the <<last inserted>> item (in versions before 3.7, a random item is removed instead)
car.popitem()
print(car)
del car["model"]
print(car)
del car # del keyword can  delete the dictionary completely