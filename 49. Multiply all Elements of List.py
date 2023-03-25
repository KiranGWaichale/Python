# 49. Write a Python program to  Multiply all numbers in the list

size = int(input("Enter size of list : "))
list = []
print("Enter list elements : ")
for i in range(size):
	list.append(int(input()))

product = 1
for ele in list:
	product = product * ele

print("Mulitplication of All List Elements is : {}".format(product))