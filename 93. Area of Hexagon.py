# 93. Given the side length x find the area of a hexagon

import math

def areaOfHexagon(length):
	area = 3 * math.sqrt(3) * 0.5 * length * length
	return round(area, 1)

length = int(input("Enter length of Hexagon (Considering Integer) : "))
print("Area of Hexagon : {}".format(areaOfHexagon(length)))