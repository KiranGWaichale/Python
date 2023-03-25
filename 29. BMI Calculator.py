# 29. Write a Python Program to calculate your Body Mass Index

def bmi(height, weight):
	return weight/(height*height)

height = float(input("Enter your Height : "))
weight = float(input("Enter your Weight : "))
print("BMI : {}".format(bmi(height, weight)))