# 59. Write a Python program to find words which are greater than given length k

def wordLength(list_of_words: list, k: int):
	output = []
	for word in list_of_words:
		if len(word) > k:
			output.append(word)

	return output

size = int(input("Enter size of the list : "))
list_of_words = []
print("Input List Elements : ")
for i in range(size):
	list_of_words.append(input())

k = int(input("Enter a length: "))

print("Words greater than {} length : {}".format(k, wordLength(list_of_words, k)))