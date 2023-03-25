# Write a Python program to swap two variables without temp variable

var1 = int(input(("Enter Varable 1: ")))
var2 = int(input(("Enter Varable 2: ")))
print("Before swap:\nvar1 = {} and var2 = {}".format(var1, var2))
var2 = var1 + var2
var1 = var2 - var1
var2 = var2 - var1
print("After swap:\nvar1 = {} and var2 = {}".format(var1, var2))