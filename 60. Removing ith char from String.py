# 60. Write a Python program for removing i-th character from a string

def removeChar(string: str, pos: int):
	new_str = str()
	for i in range(1, len(string)+1):
		if i != pos:
			new_str += string[i-1]
	return new_str

string = input("Enter a String : ")
pos = int(input("Enter position of character to remove : "))
print("String after removing {}th character : {}".format(pos, removeChar(string, pos)))