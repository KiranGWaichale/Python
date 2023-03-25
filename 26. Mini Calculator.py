# 26. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations

try:
	while True:
		num1 = int(input("Enter First Number : "))
		num2 = int(input("Enter Second Number : "))
		print("For Addition : +")
		print("For Substraction : -")
		print("For Multiplication : *")
		print("For Division : /")
		print("For Exit : X")
		ch = input("Enter the choise for Mathematical Operation : ")
		
		if ch == '+':
			output = num1 + num2
		elif ch == '-':
			output = num1 - num2
		elif ch == '*':
			output = num1 * num2
		if ch == '/':
			output = num1 / num2
		if ch == 'X':
			break
		print(output)
except Exception as e:
	print(e)