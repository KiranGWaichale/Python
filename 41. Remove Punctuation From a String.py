# 41. Write a Python Program to Remove Punctuation From a String

punctuations = ''''!()-[]{};:'\"\\,<>./?@#$%^&*_~'''
string = input("Enter the string : ")
outputString = str()
for char in string:
	if char not in punctuations:
		outputString += char

print(outputString)