# 50. Write a Python program to find smallest number in a list

size = int(input("Enter size of the list : "))
list = []
print("Input elements of the list : ")
for i in range(size):
	list.append(int(input()))

smallest = list[0]
for ele in list:
	if ele < smallest:
		smallest = ele

print("Smallest Element in Given List is : {}".format(smallest))