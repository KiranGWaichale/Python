# 42. Write a Python program to check if the given number is a Disarium Number

#def disariumNum(num):
#	try:
#		if type(num) != int:
#			raise Exception("Not an Integer")
#		num = str(num)
#		sum = 0
#		for i in range(len(num)):
#			n = int(num[i])
#			n = n**(i+1)
#			sum = sum + n
#		
#		if sum == int(num):
#			return True
#		else:
#			return False
#
#	except Exception as e:
#		print(e)
#
#num = int(input("Enter an Integer Number : "))
#if disariumNum(num):
#	print("{} is a Disarium Number.".format(num))
#else:
#	print("{} is Not a Disarium Number.".format(num))
#


def calculateLength(n):
	length = 0
	while(n != 0):
		length = length + 1
		n = n//10
	return length

num = int(input("Enter a Number : "))
digit = sum = 0
len = calculateLength(num)

temp = num

while num > 0:
	digit = num%10
	sum = sum + int(digit**len)
	num = num //10
	len = len - 1

if temp == sum:
	print("{} is a Disarium Number.".format(temp))
else:
	print("{} is Not a Disarium Number.".format(temp))