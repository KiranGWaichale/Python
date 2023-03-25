# 24. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal

def conversion(num):
	print("Binary of {} is : {}".format(num, bin(num)))
	print("Octal of {} is : {}".format(num, oct(num)))
	print("Hexadecimal of {} is : {}".format(num, hex(num)))

num = int(input("Enter a Number : "))
conversion(num)