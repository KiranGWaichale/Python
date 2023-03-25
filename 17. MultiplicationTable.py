# 17. Write a Python Program to Display the multiplication Table

num = int(input("Enter a number : "))
for i in range(1, 11, 1):
	# Below also works
	# print("{} x {} = {}".format(num, i, num*i))
	print(f"{num} x {i} = {num*i}")