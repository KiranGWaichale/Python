# 3. Write a Python Program to Print the Fibonacci sequence

fibo_length = int(input("Enter a length : "))
a = 0
b = 1
print(a, end=' ')
print(b, end=' ')
while(fibo_length-2 > 0):
	next = a + b
	print(next, end=' ')
	a = b
	b = next
	fibo_length -= 1