# 37. Write a Python Program to Add Two Matrices

r = int(input("Enter no. of Rows in Matrix : "))
c = int(input("Enter no. of Columns in Matrix : "))

mat1 = []
mat2 = []
print("Enter elements of 1st Matrix : ")
for i in range(r):
	row = []
	for j in range(c):
		row.append(int(input()))
	mat1.append(row)

print("1st Matrix : ")
for i in range(r):
	for j in range(c):
		print(mat1[i][j], end=' ')
	print()

print("Enter elements of 2nd Matrix : ")
for i in range(r):
	row = []
	for j in range(c):
		row.append(int(input()))
	mat2.append(row)

print("2nd Matrix : ")
for i in range(r):
	for j in range(c):
		print(mat2[i][j], end=' ')
	print()

result = []
for i in range(len(mat1)):
	row = []
	for j in range(len(mat1[0])):
		row.append(mat1[i][j]+mat2[i][j])
	result.append(row)
print("Resultant Matrix : {}".format(result))

# print("2nd Matrix : ")
# for i in range(r):
# 	for j in range(c):
# 		print(result[i][j], end=' ')
# 	print()