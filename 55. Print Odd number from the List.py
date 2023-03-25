# 55. Write a Python program to print odd numbers in a List

size = int(input("Enter Size of the List : "))
list = []
print("Input List Elements : ")
for i in range(0, size):
	list.append(int(input()))


print("Odd Elements from the Given List : ")
#for ele in list:
#	if ele%2 != 0:
#		print(ele, end = " ")
print([i for i in list if i%2 != 0])