# 91. Create a function that takes an angle in radians and
# returns the corresponding angle in degrees rounded to one decimal place

def radians_to_degrees(rads):
	return round(57.295779513 * rads, 1)

print(radians_to_degrees(1))
print(radians_to_degrees(20))
print(radians_to_degrees(50))