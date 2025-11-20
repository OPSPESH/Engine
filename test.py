import turtle


file = "assets/gif/sa1.gif"
turtle.register_shape(file)

turtle.shape(file)

s = turtle.Screen()
s.setup(640,480)
s.bgcolor('black')

ship = turtle.Turtle()
ship.shape("triangle")
ship.color("white")
ship.penup() 

turtle.done()