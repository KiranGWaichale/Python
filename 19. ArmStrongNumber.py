# 19. Write a Python Program to Check Armstrong Number

import math
def armstrong_check(num):
	l = len(str(num))
	sum = 0
	temp_num = num
	while(num > 0):
		d = num%10
		sum += int(math.pow(d,l))
		num //= 10 # num = num/ 10
	if(sum == int(temp_num)):
		return 1
	else:
		return 0

num = int(input("Enter a number : "))
if(armstrong_check(num)):
	print("{} is an ArmStrong number".format(num))
else:
	print("{} is not an ArmStrong number".format(num))
