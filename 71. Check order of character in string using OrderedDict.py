# 71. Write a Python program to check order of character in string using OrderedDict()

from collections import OrderedDict

def checkOrderofString(string, pattern):
	# create empty OrderedDict,
	dict = OrderedDict.fromkeys(string)
	print(dict)
	ptrlen = 0
	for key,value in dict.items():
		if (key == pattern[ptrlen]):
			ptrlen = ptrlen + 1

		# check if we have traverse complete pattern string \n",
		if (ptrlen == (len(pattern))):
			return True

	# if we come out from for loop that means order was mismatched \n",
	return False

string = input("enter string : ")
pattern = input("Enter Pattern : ")
if checkOrderofString(string, pattern):
	print("Pattern matched")
else:
	print("Pattern not matched")