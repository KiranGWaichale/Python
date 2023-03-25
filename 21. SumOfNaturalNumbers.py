# 21. Write a Python Program to Find the Sum of Natural Numbers

num = int(input("Enter a positive number : "))
total_sum = 0
for i in range(1, num+1):
	total_sum += i
print("Sum of {} natural number is {}".format(num, total_sum))