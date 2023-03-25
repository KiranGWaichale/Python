# 25. Write a Python Program To Find ASCII value of a character

try:
	char = input("Enter a character : ")
	ASCII = ord(char)
	print("ASCII of {} is : {}".format(char, ASCII))
except Exception as e:
	print(e)