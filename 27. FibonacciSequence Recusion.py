# 27. Write a Python Program to Display Fibonacci Sequence Using Recursion

def fibbo(a, b, c):
	if c>0:
		c -= 1
		print(a, end=' ')
		temp = b
		b = a+b
		a = temp
		fibbo(a, b, c)

a = 0
b = 1
c = int(input("Enter length : "))
print(fibbo(a, b, c))