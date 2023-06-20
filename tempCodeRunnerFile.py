import math
AB = float(input().strip())
BC = float(input().strip())

if 0<AB<=100 and 0<BC<=100:
    x = math.degrees(math.atan(AB/BC)) #inverse of tan (opposite/base)
    print(int(x) , chr(176), sep= '')
    #print(f'{round(x)}{chr(176)}') #character that represents the unicode 176 as (angle/degree)
else: 
    print("Out of the range of 1 to 100")