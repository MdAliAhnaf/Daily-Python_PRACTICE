person1 = dict(name='Jane Judy', sex='Female', age=28, married=False)
print(person1)

person1['address'] = '1, Penny Lane'
print(person1)
person1.pop('address')
print(person1)
print(person1.keys())
print(person1.values())
print(person1.items())

print(person1.get("name"))
print(person1.get("address", "Unknown"))
