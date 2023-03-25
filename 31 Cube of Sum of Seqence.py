# 31. Write a Python Program for cube sum of first n natural numbers

def cubeN(n):
	return sum(range(n+1))**3

n = int(input("Enter a number : "))
print(cubeN(n))