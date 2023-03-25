# 34. Write a Python Program for array rotation

arr = []
arraySize = int(input("Enter Array Size : "))
print("Enter Array Elements : ")
for i in range(0, arraySize):
	ele = int(input())
	arr.append(ele)

print("Rotated Array : {}".format(arr[::-1]))