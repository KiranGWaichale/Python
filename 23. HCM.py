# 23. Write a Python Program to Find HCF

def hcf(a, b):
	low = a if a < b else b
	for i in range(1, low+1):
		if (a%i==0) and (b%i==0):
			hcf = i
	return hcf

a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
print("HCF for {} and {} is : {}".format(a, b, hcf(a,b)))