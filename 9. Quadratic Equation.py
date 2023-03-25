# Write a Python program to solve quadratic equation

import math
print("ax^2 + bx^1 + c = 0")
print("Enter the coefficent a, b and constant c")
a = int(input(("Enter the coefficent a: ")))
b = int(input(("Enter the coefficent b: ")))
c = int(input(("Enter the constant c: ")))
d = (b**2) - (4*a*c)

if d >= 0:
	root1 = ((-1*b)+(math.sqrt(d))) / (2*a)
	root2 = ((-1*b)-(math.sqrt(d))) / (2*a)
	print("For quad eq. {}x^2 + {}x^1 + {}".format(a,b,c))
	print("The solutions are: {} and {}".format(root1, root2))    
else:
	print("Cannot find the square root of a negative number")
