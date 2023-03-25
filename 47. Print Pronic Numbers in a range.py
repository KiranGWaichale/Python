# 47. Write a Python program to print all pronic numbers between 1 and 100

i = 0
while True:
	pronicNum = i*(i+1)
	i = i+1
	if pronicNum > 100:
		break
	print(pronicNum, end = " ")