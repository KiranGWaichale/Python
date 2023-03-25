# 87. Please write a program using list comprehension to print the Fibonacci Sequence in comma separated
# form with a given n input by console

def fibo(n):
	i = 0
	j = 1
	for k in range(n+1):
		yield i
		i,j = j, i+j

n = int(input("Enter number : "))
print(', '.join([str(i) for i in fibo(n)]))