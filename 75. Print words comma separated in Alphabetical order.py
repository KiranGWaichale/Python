# 75. Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.

words = list(input("Enter comma separted words : ").split(','))
words.sort()

print(','.join(words))