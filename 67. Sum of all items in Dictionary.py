# 67. Write a Python program to find the sum of all items in a dictionary

test_dict = {'k1' : 89,
	'k2' : 111,
	'k3' : 123,
	'k4' : 5}

sum = 0
for i in test_dict.values():
	sum += i
print("Sum of all values is : {}".format(sum))