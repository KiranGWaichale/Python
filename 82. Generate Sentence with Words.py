# 82. Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ['Play', "Love"]
# and the object is in ["Hockey","Football"]."

subject = ["I", "You"]
verb = ["Play", "Love"]
obj = ["Hockey", "Football"]
sentence_list = []

for s in subject:
	for v in verb:
		for o in obj:
			sentence_list.append(s+" "+v+" "+o)

for sentence in sentence_list:
	print(sentence)