# 45. Write a Python program to print all happy numbers between 1 and 100

def check(num):
	res = num
	def isHappy(num):
		r = s = 0
		while num>0:
			r = num%10
			s = s + r**2
			num = num//10
		return s

	while (res!=1 and res !=4):
		res = isHappy(res)

	if res == 1:
		return True
	elif res == 4:
		return False

low = int(input("Enter low : "))
high = int(input("Enter high : "))
for i in range(low, high+1):
	if check(i):
		print(i, end = " ")