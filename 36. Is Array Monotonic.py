# 36. Write a Python Program to check if given array is Monotonic

def monotonicCheck(array):
	return (all(array[i] <= array[i + 1] for i in range(len(array) - 1)) or
		all(array[i] >= array[i + 1] for i in range(len(array) - 1)))

arr = []
arraySize = int(input("Enter Array Size : "))
print("Enter Array Elements : ")
for i in range(0, arraySize):
	ele = int(input())
	arr.append(ele)

# print(len(arr))
# for i in range(len(arr)):
# 	print("arr[{}] = {}".format(i, arr[i]))

if monotonicCheck(array = arr):
	print("Array is Monotonic")
else:
	print("Array is Not Monotonic")