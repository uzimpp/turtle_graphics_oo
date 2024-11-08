import turtle
import random

reduction_ratio = 0.618

class Run():
	def __init__(self, n) -> None:
		self.__n = n
	
	@property
	def n(self):
		return self.__n
	
	@n.setter
	def n(self, n):
		self.__n = n


	def draw_multiple(self):
		for _ in range(30):
			if 5 <= self.__n <= 9:
				polygon = EmbeddedPolygon(self.__n)
				polygon.draw_polygon()
			else:
				polygon = Polygon(self.__n)
				polygon.draw_polygon()

		
class Polygon():
	def __init__(self, n) -> None:
		self.n = n
		self.num_sides = self.determine_num_sides()
		self.size = random.randint(50, 150)
		self.orientation = random.randint(0, 90)
		self.location = [random.randint(-300, 300), random.randint(-200, 200)]
		self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
		self.border_size = random.randint(1, 10)

	def determine_num_sides(self):
		if self.n in [4, 8, 9]:
			return random.randint(3, 5)
		if self.n in [1, 5]:
			return 3
		if self.n in [2, 6]:
			return 4
		if self.n in [3, 7]:
			return 5
		return 3

	def draw_polygon(self):
		turtle.penup()
		turtle.goto(self.location[0], self.location[1])
		turtle.setheading(self.orientation)
		turtle.color(self.color)
		turtle.pensize(self.border_size)
		turtle.pendown()
		self.draw()
		turtle.penup()
	
	def draw(self):
		for _ in range(self.num_sides):
			turtle.forward(self.size)
			turtle.left(360/self.num_sides)

class EmbeddedPolygon(Polygon):
	def draw_polygon(self):
		if self.n == 9:
			depth = random.randint(0, 3)
		else:
			depth = 3
		for _ in range(1, depth + 1):
			turtle.penup()
			turtle.goto(self.location[0], self.location[1])
			turtle.setheading(self.orientation)
			turtle.right(90 + (180/self.num_sides))
			turtle.forward((self.size / reduction_ratio) - self.size)
			turtle.color(self.color)
			turtle.pensize(self.border_size)
			turtle.pendown()
			turtle.setheading(self.orientation)
			self.draw()
			self.size *= reduction_ratio
			turtle.penup()


turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

while(True):
	n = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
	turtle.clear()
	if n == 0:
		break
	elif 1 <= n <= 9:
		run = Run(n)
		run.draw_multiple()
	else:
		print("Please try again")

turtle.done()