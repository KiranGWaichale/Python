# 65. Write a Python Program to check if a string contains any special character

import re
string = input("Enter a String : ")
regex = re.compile('[@_!#$%^&*()<>?/\\|}{~:]')
if (regex.search(string) == None):
	print("Given String does not contain Special Characters")
else:
	print("Given String contains Special Characters")