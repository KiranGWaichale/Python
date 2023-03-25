# 84. Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

def binarySearch(list1: list, n: int):
	low = 0
	high = len(list1) - 1
	mid = 0
	
	while low <= high:
		mid = (high + low) //2
		if list1[mid] < n:
			low = mid + 1
		elif list1[mid] > n:
			high = mid - 1
		else:
			return mid
	return -1


print("Pre-requiste is a Sorted list !!")
str = input("Input list with comma separted values: ")
input_list = str.split(',')

sorted_list = []
for i in input_list:
	sorted_list.append(int(i))

key = int(input("Enter key to search : "))
print("Key found at Index : {}".format(binarySearch(list1=sorted_list, n=key)))