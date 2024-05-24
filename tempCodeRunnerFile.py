persons = [{'name': 'John', 'sex': 'Male'}, {'name': 'Jane', 'sex': 'Female'}]

for x in persons:
    for key in x:
        print(key, ":", x[key])
    print(" ")