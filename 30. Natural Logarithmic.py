# 30. Write a Python Program to calculate the natural logarithm of any number

import math
try:
	num = int(input("Enter a Number : "))
	print(math.log(num))
except Exception as e:
	print(e)