# 92. In this challenge, establish if a given integer num is a Curzon number.
# If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
# Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

def isCurzonNumber(n):
	if(1 + 2 ** n) % (1 + 2 * n) == 0:
		return True
	return False

n = int(input("Enter a Number : "))
print(isCurzonNumber(n))