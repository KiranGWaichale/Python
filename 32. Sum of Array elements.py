# 32. Write a Python Program to find sum of array

arr = []
size = int(input("Enter Size of Array : "))
print("Enter Array Elements : ")
for i in range(0, size):
	ele = int(input())
	arr.append(ele)

arraySum = 0
for i in arr:
	arraySum += i

print("Sum of Array Element is : {}".format(arraySum))