# 51. Write a Python program to find largest number in a list

size = int(input("Enter size of the list : "))
list = []
print("Input elements of the list : ")
for i in range(size):
	list.append(int(input()))

largest = list[0]
for ele in list:
	if ele > largest:
		largest = ele

print("Largest Element in Given List is : {}".format(largest))