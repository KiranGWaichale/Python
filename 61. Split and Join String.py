# 61. Write a Python program to split and join a string

def splitAndJoin(string: str):
	split = string.split(' ')
	print(split)
	join = " ".join(split)
	print(join)

string = input("Enter a String : ")
splitAndJoin(string)