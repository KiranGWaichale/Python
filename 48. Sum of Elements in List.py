# 48. Write a Python program to find sum of elements in list

size = int(input("Enter size of the List: "))
list = []
print("Enter List Elements : ")
for i in range(size):
	list.append(int(input()))

sum = 0
for i in list:
	sum=sum + i

print("Sum of Element in list = {}".format(sum))