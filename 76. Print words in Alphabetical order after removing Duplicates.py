# 76. Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically

# words = list(input("Enter words comma separated : ").split(' '))
# words.sort()
# setOfWords = set(words)
# print(" ".join(setOfWords))


words = list(set(input("Enter words comma separated : ").split(' ')))
words.sort()
print(" ".join(words))