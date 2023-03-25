# 53. Write a Python program to find N largest elements from a list

size = int(input("Enter size of the list : "))
list = []
print("Input elements of the list : ")
for i in range(size):
	list.append(int(input()))

list.sort(reverse=True)
n = int(input("Enter Nto find Nth Largest Element in List : "))
print("{}th Largest Element is : {}".format(n, list[n-1]))