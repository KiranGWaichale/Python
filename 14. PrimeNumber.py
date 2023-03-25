# 14. Write a Python Program to Check Prime Number

num = int(input("Enter a number: "))

isPrime = True
if num <= 1:
	print(f"{num} is neither prime nor composite")
else:
	d = 2
	while(d*d <= num):
		if(num%d==0):
			isPrime = False
			break
		d = d + 1

if(num > 1):
	if(isPrime):
		print(f"{num} is prime number")
	else:
		print(f"{num} is not prime number")