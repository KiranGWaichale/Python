# 64. Write a Python to find all duplicate characters in string

def duplicateChar(string: str):
	duplicate = []
	for ch in string:
		if string.count(ch) > 1:
			duplicate.append(ch)

	return set(duplicate)


string = input("Enter a String : ")
print("Duplicate characters in Given String : {}".format(duplicateChar(string)))