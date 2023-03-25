# 44. Write a Python program to check if the given number is Happy Number

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

num = int(input("Enter a Number : "))
if check(num):
	print("{} is a Happy Number".format(num))
else:
	print("{} is Not a Happy Number".format(num))