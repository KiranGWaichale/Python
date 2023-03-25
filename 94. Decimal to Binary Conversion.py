# 94. Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128

def binary(n):
	return "{0:b}".format(int(n))

# print(binary(1))
# print(binary(5))
# print(binary(10))
n = int(input("Enter a Decimal Number : "))
print(binary(n))