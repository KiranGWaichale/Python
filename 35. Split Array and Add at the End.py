# 4. Write a Python Program to Split the array and add the first part to the end

def splitAdd(arr, split):
	out = []
	for i in range(len(arr)):
		index = (i+len(arr)+split)%len(arr)
		out.append(arr[index])
	return out

arr = []
arraySize = int(input("Enter Array Size : "))
print("Enter Array Elements : ")
for i in range(0, arraySize):
	ele = int(input())
	arr.append(ele)

split = int(input("Enter Split Index : "))
print(splitAdd(arr=arr, split=split))