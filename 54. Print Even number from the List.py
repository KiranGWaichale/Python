# 54. Write a Python program to print even numbers in a list

size = int(input("Enter Size of the List : "))
list = []
print("Input List Elements : ")
for i in range(0, size):
	list.append(int(input()))

print("Even Elements from the Given List : ")
for ele in list:
	if ele%2 == 0:
		print(ele, end = " ")