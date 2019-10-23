import turtle 

my_turtle = turtle.Turtle()

def square(length, angle):
	my_turtle.forward(length)
	my_turtle.left(angle)
	my_turtle.forward(length)
	my_turtle.left(angle)
	my_turtle.forward(length)
	my_turtle.left(angle)
	my_turtle.forward(length)
	my_turtle.left(angle)

def angle_speed(m,n):
	my_turtle.left(m)
	my_turtle.speed(n)

for i in range(36):
	square(100,90)
	angle_speed(10,10)

for i in range(72):
	square(100,90)
	angle_speed(5,10)	

turtle.done() 
