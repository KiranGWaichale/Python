# 46. Write a Python program to determine whether the given number is a Harshad Number

def isHarshadNumber(num):
	temp = num
	base = 0
	while temp > 0:
		base = base + (temp%10)
		temp = temp//10
	
	if num%base == 0:
		return True
	else:
		return False

num = int(input("Enter a Number : "))
if isHarshadNumber(num):
	print("{} is a Harshad Number".format(num))
else:
	print("{} is Not a Harshad Number".format(num))