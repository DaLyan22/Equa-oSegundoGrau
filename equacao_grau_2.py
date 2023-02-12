#!/usr/bin/python3


import cmath


a = 1
b = 5
c = 6


d = (b**2) - (4*a*c)


raiz1 = (-b-cmath.sqrt(d))/(2*a)
raiz2 = (-b+cmath.sqrt(d))/(2*a)

print('As raízes são:')
print(raiz1)
print(raiz2)
    