# 52. Write a Python program to find second largest number in a list

size = int(input("Enter size of the list : "))
list = []
print("Input elements of the list : ")
for i in range(size):
	list.append(int(input()))

list.sort(reverse=True)

print("Second Largest Element in Given List is : {}".format(list[1]))