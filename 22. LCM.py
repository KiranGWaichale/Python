# 22. Write a Python Program to Find LCM

# Function which return the LCM of two number.
def lcm(a,b):
	high = a if a > b else b
	while True:
		if (high%a==0) and (high%b==0):
			break
		else:
			high += 1
	return high

a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("LCM of {} and {} is : {}".format(a, b, lcm(a, b)))