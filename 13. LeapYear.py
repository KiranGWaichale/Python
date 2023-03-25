# 13. Write a Python Program to Check Leap Year

year = int(input("Enter a Year : "))

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
	print(f"{year} is a Leap Year")
else:
	print(f"{year} is Not a Leap Year")