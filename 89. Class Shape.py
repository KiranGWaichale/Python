# 89. Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default

class Shape():
	def __init__(self, length):
		self.length = length

	def area(self):
		return 0

class Square(Shape):
	def area(self):
		return self.length*self.length

shape_obj = Shape(10)
print("Area of Shape : {}".format(shape_obj.area()))

square_obj = Square(13)
print("Area of Square : {}".format(square_obj.area()))