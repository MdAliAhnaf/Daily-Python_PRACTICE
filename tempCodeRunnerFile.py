class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):                     # The string representation of an object WITH the __str__() function
    return f"NAME:{self.name} AGE:({self.age})"

myobjectp1 = Person("John", 36)

print(myobjectp1)