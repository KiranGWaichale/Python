# 16. Write a Python Program to Find the Factorial of a Number

num = int(input("Enter a number : "))
fact = 1
for i in range(num, 0, -1):
	fact = fact*i
print("Factorial of {} is: {}".format(num, fact))