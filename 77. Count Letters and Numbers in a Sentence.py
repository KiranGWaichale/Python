# 77. Write a program that accepts a sentence and calculate the number of letters and digits

sentence = input("Enter a Sentence : ")
letters = digits = 0
for c in sentence:
	if(ord(c)>=ord('a') and ord(c)<=ord('z')) or (ord(c)>=ord('A') and ord(c)<=ord('Z')):
		letters += 1
	elif (ord(c)>=ord('0') and ord(c)<=ord('9')):
		digits += 1

print("Letters : {}".format(letters))
print("Digits : {}".format(digits))