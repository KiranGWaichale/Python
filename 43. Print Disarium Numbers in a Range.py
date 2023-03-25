# 43. Write a Python program to print all disarium numbers between 1 to 100

def calculateLength(n):
	length = 0
	while n != 0:
		length = length + 1
		n = n//10
	return length

def disariumNum(n):
	digit = sum = 0
	len = calculateLength(n)
	temp = n
	while n != 0:
		digit= n%10
		sum = sum + int(digit**len)
		len = len - 1
		n= n//10

	if temp == sum:
		return True
	else:
		return False

lower = int(input("Enter low : "))
higher = int(input("Enter high : "))

for i in range(lower, higher+1):
	if(disariumNum(i)):
		print(i, end=" ")