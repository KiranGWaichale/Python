# 20. Write a Python Program to Find Armstrong Number in an Interval

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

low = int(input("Enter the lower value of range : "))
high = int(input("Enter the higher value of range : "))
print("From {} to {} following are the Armstrong Numbers : ".format(low, high))
for i in range(low, high+1):
	if(armstrong_check(i)):
		print(i, end=' ')