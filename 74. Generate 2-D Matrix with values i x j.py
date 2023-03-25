# 74. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j

x = int(input("Enter value of x : "))
y = int(input("Enter value of y : "))
matrix = []

for i in range(x):
	row= []
	for j in range(y):
		row.append(i*j)
	matrix.append(row)

print("2-D Matrix : ")
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		print(matrix[i][j], end = " ")
	print()