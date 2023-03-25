# 62. Write a Python to check if a given string is binary string or not

string = input("Enter a String : ")
binary = ['0', '1']
isBinary = True
for i in string:
	if i not in binary:
		isBinary = False
		break;

if isBinary:
	print("Given String {} is Binary".format(string))
else:
	print("Given String {} is Not a Binary".format(string))