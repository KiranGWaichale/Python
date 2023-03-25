# 58. Write a Python program to Count occurrences of an element in a list

size = int(input("Enter size of the list : "))
list = []
print("Input List Elements : ")
for i in range(0, size):
	list.append(int(input()))

ele = int(input("Enter Element to find : "))
count = 0
for i in list:
	if i == ele:
		count += 1

print("Occurrence of {} in Given list is : {}".format(ele, count))