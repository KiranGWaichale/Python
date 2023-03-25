# 11. Write a Python Program to Check if a Number is Positive, Negative or Zero

num = input("Enter a Number : ")
if (int(num) > 0):
	print(f"{num} is Positive Number")
elif (int(num) < 0):
	print(f"{num} is Negative Number")
else:
	print(f"{num} is Zero")