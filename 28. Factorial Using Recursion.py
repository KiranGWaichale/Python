# 28. Write a Python Program to Find Factorial of Number Using Recursion

def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)

num = int(input("Enter a number : "))
print("Factorial of {} is : {}".format(num, fact(num)))