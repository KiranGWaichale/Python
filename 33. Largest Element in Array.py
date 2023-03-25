# 33. Write a Python Program to find largest element in an array

arr = []
arraySize = int(input("Enter Array Size : "))
print("Enter Array Elements : ")
for i in range(0, arraySize):
	ele = int(input())
	arr.append(ele)

largest = -9999999999999
for i in arr:
	if i > largest:
		largest = i

print("Larget Element in given Array is : {}".format(largest))