# 74. Write a program that calculates and prints the value according to the given formula:
#   Q = Square root of [(2 C D)/H]
#   Following are the fixed values of C and H:
#   C is 50. H is 30.
#   D is the variable whose values should be input to your program in a comma-separated sequence.
#   Example
#   Let us assume the following comma separated input sequence is given to the program:
#   100,150,180
#   The output of the program should be:
#   18,22,24

import math

def calculateFun(listOfIntValues):
	# Formaula for Calculation = sq.root[(2CD)/H]
	# print("Formaula for Calculation = sq.root[(2CD)/H]")
	# print("Values; C = 50, H = 30")

	c = 50
	h =30
	result = []
	for d in listOfIntValues:
		result.append(int(math.sqrt((2*c*int(d))/h)))

	print("Result : {}".format(result))



print("Formula for Calculation = sq.root[(2CD)/H]")
print("Pre-defined Values; C = 50, H = 30")
listOfIntValues = list(input("Enter 'd' values speartaed by comma : ").split(','))
calculateFun(listOfIntValues)