import keyboard, time
from turtle import *

class body:
    def __init__(self, char_type, turtle):
        self.type = char_type
        self.turtle = turtle
        
    def switch_sides(self):
        screen.tracer(0)
        if self.turtle.xcor() >= 320:
            self.turtle.setpos(-320, self.turtle.ycor())
        elif self.turtle.xcor() <= -330:
            self.turtle.setpos(310, self.turtle.ycor())
        if self.turtle.ycor() >= 220:
            self.turtle.setpos(self.turtle.xcor(), -230)
        elif self.turtle.ycor() <= -230:
            self.turtle.setpos(self.turtle.xcor(), 220)
        screen.tracer(1)

class bullet:
    def __init__(self, turtle, distance):
        self.turtle = turtle
        self.range = distance
        self.turtle.showturtle()
        self.turtle.goto(ship.xcor(), ship.ycor())
    
    def fire(self):
        self.range -= 10
        self.turtle.forward(10)
        print(self.range)
        if self.range <= 0:
            bullets[1] = 0

     
ship = Turtle()
ship.shape("triangle")
ship.color("white")
ship.penup() 

ship_controller = body("player", ship)

bullets = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0
}


bt1 = Turtle()
bt1.shape("circle")
bt1.color("red")
bt1.penup()
bt1.hideturtle()



screen = Screen()
screen.setup(640,480)
screen.bgcolor('black')


def astroids_mainloop():
    while True:
        screen.tracer(0)
        if keyboard.is_pressed("w"):
            ship.forward(5)
        if keyboard.is_pressed("a"):
            ship.left(15)
        if keyboard.is_pressed("d"):
            ship.right(15)
        if keyboard.is_pressed("space"):
            b1 = bullet(bt1, 200)
            bullets[1] = 1

        if bullets[1] == 1:
            b1.fire() 
        
        
        
        
        
        ship_controller.switch_sides()
        time.sleep(0.05)
        screen.tracer(1)


astroids_mainloop()
screen.exitonclick()