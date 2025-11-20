from turtle import *
import turtle

s = Screen()
s.setup(640,480)
s.bgcolor('black')
s.tracer(0)

ship = Turtle()
ship.shape("triangle")
ship.color("white")
ship.penup() 

b1 = Turtle()
b1.shape("circle")
b1.color("red")
b1.penup()
b1.hideturtle()
b1.turtlesize(0.5)

b2 = Turtle()
b2.shape("circle")
b2.color("red")
b2.penup()
b2.hideturtle()
b2.turtlesize(0.5)

b3 = Turtle()
b3.shape("circle")
b3.color("red")
b3.penup()
b3.hideturtle()
b3.turtlesize(0.5)

b4 = Turtle()
b4.shape("circle")
b4.color("red")
b4.penup()
b4.hideturtle()
b4.turtlesize(0.5)

b5 = Turtle()
b5.shape("circle")
b5.color("red")
b5.penup()
b5.hideturtle()
b5.turtlesize(0.5)


turtle.register_shape("assets/gif/ba0.gif")
turtle.register_shape("assets/gif/ba1.gif")
turtle.register_shape("assets/gif/ba2.gif")
turtle.register_shape("assets/gif/sa0.gif")
turtle.register_shape("assets/gif/sa1.gif")
turtle.register_shape("assets/gif/sa2.gif")
turtle.register_shape("assets/gif/enemy.gif")







s.tracer(1)