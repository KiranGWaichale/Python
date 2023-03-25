# 2. Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically

def frequencyCount(string: str):
	str_list = str.split(' ')
	out_dict = {}
	for s in str_list:
		if s in out_dict.keys():
			out_dict[s] += 1
		else:
			out_dict[s] = 1

	for k, v in sorted(out_dict.items()):
		print(k,' : ',v)

str = input("Enter a Sentence : ")
frequencyCount(str)