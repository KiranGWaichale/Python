# 85. Please write a program using generator to print the numbers which can be divisible by 5 and 7
# between 0 and n in comma separated form while n is input by console

def generator(n: int):
	for i in range(n+1):
		if i%5==0 and i%7==0:
			yield str(i)+' '

n = int(input("Enter the Max : "))
print(generator(n))
# l = generator(n)
# for i in l:
# 	print(i, end = ",")

print(', '.join([i for i in generator(n)]))