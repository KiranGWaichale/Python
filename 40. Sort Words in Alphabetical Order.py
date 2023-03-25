# 40. Write a Python Program to Sort Words in Alphabetic Order

try:
	sentence = input("Enter the words (Separted by Space) : ")
	words = [word.lower() for word in sentence.split()]
	words.sort()
	
	print("Sorted oder of words : ")
	for word in words:
		print(word, end = " ")

except Exception in e:
	print(e)