# 1. Define a class with a generator which can iterate the numbers,which are divisible by 7,
# between a given range 0 and n."

class Demo:
	def gen(self, n):
		for i in range(n+1):
			if i%7 == 0:
				yield i


nums = Demo()
n = int(input("Enter Max : "))
print([i for i in nums.gen(n)])