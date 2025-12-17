from turtle import *
import turtle

# Register image shapes used for astroids and enemy
turtle.register_shape("assets/ba0.gif")  # big asteroid 0
turtle.register_shape("assets/ba1.gif")  # big asteroid 1
turtle.register_shape("assets/ba2.gif")  # big asteroid 2
turtle.register_shape("assets/sa0.gif")  # small asteroid 0
turtle.register_shape("assets/sa1.gif")  # small asteroid 1
turtle.register_shape("assets/sa2.gif")  # small asteroid 2
turtle.register_shape("assets/enemy.gif")  # alien/enemy ship

# Screen configuration
s = Screen()
s.setup(640,480)      # window size
s.bgcolor('black')    # background colour
s.tracer(0)           # disable automatic drawing updates for batch rendering

# Main player ship turtle setup
ship = Turtle()
ship.shape("turtle")
ship.color("white")
ship.penup()          # don't draw lines when moving

# Alien turtle (hidden until spawned)
alien = Turtle()
alien.shape("assets/enemy.gif")
alien.penup()
alien.hideturtle()

# Life indicator turtles (top-left of screen)
life1 = Turtle()
life1.shape("turtle")
life1.color("white")
life1.left(90)
life1.penup()
life1.goto(-250, 210)

life2 = Turtle()
life2.shape("turtle")
life2.color("white")
life2.left(90)
life2.penup()
life2.goto(-275, 210)

life3 = Turtle()
life3.shape("turtle")
life3.color("white")
life3.left(90)
life3.penup()
life3.goto(-300, 210)

# Score display turtle (top-left)
score = Turtle()
score.pencolor("white")
score.hideturtle()
score.penup()
score.goto(-307, 170)
# score.write(1000, font=("Comic Sans", 16, "bold"))  # example usage

# Bullet turtle pool (b0..b4) - pre-created, hidden, reused when firing
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

# Astroid turtles pool (a0..a14) - pre-created, hidden, reused when spawning astroids
a0 = Turtle();  a0.penup();  a0.hideturtle()
a1 = Turtle();  a1.penup();  a1.hideturtle()
a2 = Turtle();  a2.penup();  a2.hideturtle()
a3 = Turtle();  a3.penup();  a3.hideturtle()
a4 = Turtle();  a4.penup();  a4.hideturtle()
a5 = Turtle();  a5.penup();  a5.hideturtle()
a6 = Turtle();  a6.penup();  a6.hideturtle()
a7 = Turtle();  a7.penup();  a7.hideturtle()
a8 = Turtle();  a8.penup();  a8.hideturtle()
a9 = Turtle();  a9.penup();  a9.hideturtle()
a10 = Turtle(); a10.penup(); a10.hideturtle()
a11 = Turtle(); a11.penup(); a11.hideturtle()
a12 = Turtle(); a12.penup(); a12.hideturtle()
a13 = Turtle(); a13.penup(); a13.hideturtle()
a14 = Turtle(); a14.penup(); a14.hideturtle()

# Re-enable tracer for normal drawing (main loop toggles this for frame updates)
s.tracer(1)
# s.exitonclick()  # optional: keep window open until click (not used in game loop)