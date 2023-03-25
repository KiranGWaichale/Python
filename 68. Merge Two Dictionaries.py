# 68. Write a Python program to Merging two Dictionaries

dict1 = { 'x': 1, 'l': 2}
dict2 = { 'k': 3, 'z': 4, 'x': 11}
# merging dict2 into dict1
for item in dict2.items():
	dict1.setdefault(item[0], item[1])
print(dict1)