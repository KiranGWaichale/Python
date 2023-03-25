# 63. Write a Python program to find uncommon words from two Strings

def uncommonCheck(str1: str, str2: str):
	#str1 = str1.lower()
	#str2 = str2.lower()
	str1 = str1.split(' ')
	str2 = str2.split(' ')
	uncommon = []
	
	for word in set(str1):
		if word not in str2:
			uncommon.append(word)

	for word in set(str2):
		if word not in str1:
			uncommon.append(word)

	return uncommon

str1 = input("Enter String 1 : ")
str2 = input("Enter String 2 : ")
if len(uncommonCheck(str1, str2)) != 0:
	print("Uncommon words in given strings are : {}".format(uncommonCheck(str1, str2)))
else:
	print("Both the strings are Same.")
