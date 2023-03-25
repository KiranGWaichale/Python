# 38. Write a Python Program to Multiply Two Matrices

r1 = int(input("Enter no. of Rows in Matrix1 : "))
c1 = int(input("Enter no. of Columns in Matrix1 : "))

mat1 = []
print("Enter elements of 1st Matrix : ")
for i in range(r1):
	row = []
	for j in range(c1):
		row.append(int(input()))
	mat1.append(row)

print("1st Matrix : ")
for i in range(r1):
	for j in range(c1):
		print(mat1[i][j], end=' ')
	print()

r2 = int(input("Enter no. of Rows in Matrix2 : "))
c2 = int(input("Enter no. of Columns in Matrix2 : "))

mat2 = []
print("Enter elements of 2nd Matrix : ")
for i in range(r2):
	row = []
	for j in range(c2):
		row.append(int(input()))
	mat2.append(row)

print("2nd Matrix : ")
for i in range(r2):
	for j in range(c2):
		print(mat2[i][j], end=' ')
	print()

result = []
for i in range(r1):
	row = []
	for j in range(c2):
		row.append(0)
	result.append(row)

if c1 == r2:
	for i in range(len(mat1)):
		for j in range(len(mat2[0])):
			for k in range(len(mat2)):
				result[i][j] += mat1[i][k] * mat2[k][j]

	print("Resultant Matrix : ")
	for i in range(len(result)):
		for j in range(len(result[0])):
			print(result[i][j], end=' ')
		print()
else:
	print("Can not perform Matrix Mulitplication!!!")