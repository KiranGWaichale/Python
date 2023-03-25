# 56. Write a Python program to Remove empty List from List

l = [[], 12, 31, [1,2, -23] , [1], [], [123.23], [], 2, 321]
result = []
for i in l:
	if type(i) == list:
		if len(i) != 0:
			result.append(i)
	else:
		result.append(i)

print(result)