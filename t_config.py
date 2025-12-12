from turtle import *
import turtle

loaded = 0
turtle.register_shape("assets/ba0.gif")
turtle.register_shape("assets/ba1.gif")
turtle.register_shape("assets/ba2.gif")
turtle.register_shape("assets/sa0.gif")
turtle.register_shape("assets/sa1.gif")
turtle.register_shape("assets/sa2.gif")
turtle.register_shape("assets/enemy.gif")

s = Screen()
# s.setup(640,480)
s.bgcolor('black')
s.tracer(0)

ship = Turtle()
ship.shape("turtle")
ship.color("white")
ship.penup() 

alien = Turtle()
alien.shape("assets/enemy.gif")
alien.penup()
alien.hideturtle()


b0 = Turtle()
b0.shape("circle")
b0.color("red")
b0.penup()
b0.hideturtle()
b0.turtlesize(0.5)

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

a0 = Turtle()
a0.penup()
a0.hideturtle()

a1 = Turtle()
a1.penup()
a1.hideturtle()

a2 = Turtle()
a2.penup()
a2.hideturtle()

a3 = Turtle()
a3.penup()
a3.hideturtle()

a4 = Turtle()
a4.penup()
a4.hideturtle()

a5 = Turtle()
a5.penup()
a5.hideturtle()

a6 = Turtle()
a6.penup()
a6.hideturtle()

a7 = Turtle()
a7.penup()
a7.hideturtle()

a8 = Turtle()
a8.penup()
a8.hideturtle()

a9 = Turtle()
a9.penup()
a9.hideturtle()

a10 = Turtle()
a10.penup()
a10.hideturtle()

a11 = Turtle()
a11.penup()
a11.hideturtle()

a12 = Turtle()
a12.penup()
a12.hideturtle()

a13 = Turtle()
a13.penup()
a13.hideturtle()

a14 = Turtle()
a14.penup()
a14.hideturtle()

s.tracer(1)
loaded = 1