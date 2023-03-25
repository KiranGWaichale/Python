# 86. Please write a program using generator to print the even numbers between 0 and n in comma separated
# form while n is input by console

def printEven(n: int):
	for i in range(n+1):
		if i%2==0:
			yield str(i)

n = int(input("Enter max : "))
print(f"Generator : {printEven(n)}")
print(','.join([i for i in printEven(n)]))