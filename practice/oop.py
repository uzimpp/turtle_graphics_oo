import turtle
import random
import math

class PolygonArt():
	def __init__(self, n) -> None:
		self.__n = n
		turtle.speed(0)
		turtle.bgcolor('black')
		turtle.tracer(0)
		turtle.colormode(255)

	def getval(self):
		size = random.randint(50, 150)
		orientation = random.randint(0, 90)
		location = [random.randint(-300, 300), random.randint(-200, 200)]
		color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
		border_size = random.randint(1, 10)
		return size, orientation, location, color, border_size,
		
	def run(self):
		for _ in range(25):
			size, orientation, location, color, border_size = self.getval()
			num_sides = 3
			if self.__n == 4 or self.__n == 9:
				num_sides = random.randint(3, 5)
			elif self.__n == 3 or self.__n == 7:
				num_sides = 5
			elif self.__n == 2 or self.__n == 6:
				num_sides = 4

			if 5 <= self.__n <= 9:
				depth = 3
				if self.__n == 9:
					depth = random.randint(0, 3)
				p = EmbbedPolygon(num_sides, size, orientation, location, color, border_size, depth)
			elif 1 <= self.__n <= 4:
				p = Polygon(num_sides, size, orientation, location, color, border_size)
			p.draw()
			
			

class Polygon():
	def __init__(self, num_sides, size, orientation, location, color, border_size) -> None:
		self.__num_sides = num_sides
		self.__size = size
		self.__orientation = orientation
		self.__location = location
		self.__color = color
		self.__border_size = border_size
	
	@property
	def num_sides(self):
		return self.__num_sides

	@property
	def size(self):
		return self.__size
		
	@size.setter
	def size(self, val):
		self.__size = val

	@property
	def orientation(self):
		return self.__orientation
		
	@property
	def location(self):
		return self.__location

	@property
	def color(self):
		return self.__color

	@property
	def border_size(self):
		return self.__border_size

	def draw(self):
		turtle.penup()
		turtle.goto(self.__location[0], self.__location[1])
		turtle.setheading(self.__orientation)
		turtle.color(self.__color)
		turtle.pensize(self.__border_size)
		turtle.pendown()
		for _ in range(self.__num_sides):
			turtle.forward(self.__size)
			turtle.left(360/self.__num_sides)
		turtle.penup()

class EmbbedPolygon(Polygon):
	def __init__(self, num_sides, size, orientation, location, color, border_size, depth) -> None:
		super().__init__(num_sides, size, orientation, location, color, border_size)
		self.__depth = depth
		self.__reduction_ratio = 0.618
		
	def draw(self):
		angle = 360 / self.num_sides
		for _ in range(self.__depth + 1):
			turtle.penup()
			turtle.goto(self.location[0], self.location[1])
			turtle.setheading(self.orientation)
			turtle.color(self.color)
			turtle.pensize(self.border_size)
			turtle.right(90 + (180 / self.num_sides))
			turtle.backward(self.size - (self.size / self.__reduction_ratio))
			turtle.setheading(self.orientation)
			turtle.pendown()
			for _ in range(self.num_sides):
				turtle.forward(self.size)
				turtle.left(360 / self.num_sides)
			turtle.penup()
			self.size *= self.__reduction_ratio
			
while(True):
	n = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
	turtle.clear()
	if n == 0:
		break
	elif 1 <= n <= 9:
		art = PolygonArt(n)
		art.run()
	else:
		print("Please try again")

turtle.done()