# 39. Write a Python Program to Transpose a Matrix

r = int(input("Enter No. of Rows in Matrix : "))
c = int(input("Enter No. of Colums in Matrix : "))
matrix = []

print("Input {} x {} Matrix Elements : ".format(r, c))
for i in range(r):
	row = []
	for j in range(c):
		row.append(int(input()))
	matrix.append(row)

print("Given Matrix : ")
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		print(matrix[i][j], end=" ")
	print()

transpose = []
#for i in range(c):
#	row = []
#	for j in range(r):
#		row.append(0)
#	transpose.append(row)

for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		transpose[j][i] = matrix[i][j]

print("Transpose Matrix : ")
for i in range(len(transpose)):
	for j in range(len(transpose[0])):
		print(transpose[i][j], end=" ")
	print()
