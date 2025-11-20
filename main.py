import t_config as t
import time as ti
import keyboard as k

class body:
    def __init__(self, char_type, turtle):
        self.type = char_type
        self.turtle = turtle
        
    def switch_sides(self):
        if self.turtle.xcor() >= 320:
            self.turtle.setpos(-320, self.turtle.ycor())
        elif self.turtle.xcor() <= -330:
            self.turtle.setpos(310, self.turtle.ycor())
        if self.turtle.ycor() >= 220:
            self.turtle.setpos(self.turtle.xcor(), -230)
        elif self.turtle.ycor() <= -230:
            self.turtle.setpos(self.turtle.xcor(), 220)


class bullet:
    def __init__(self, turtle, distance, instance):
        self.turtle = turtle
        self.range = distance
        self.instance = instance
        self.turtle.showturtle()
        self.turtle.goto(t.ship.xcor(), t.ship.ycor())
        self.turtle.setheading(t.ship.heading())
    def fire(self):
        self.range -= 10
        self.turtle.forward(15)
        if self.range <= 0:
            bullets[self.instance] = 0
            self.turtle.hideturtle()
            del self

bullets = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
}

def spawn_bullet():
    global b1,b2,b3,b4,b5
    b=0
    for i in range(1,6):
        select = bullets[i]
        if select == 0:
            b = i
            bullets[i] = 1
            break
    match b:
        case 1:
            b1 = bullet(t.b1, 200, 1)
        case 2:
            b2 = bullet(t.b2, 200, 2)
        case 3:
            b3 = bullet(t.b3, 200, 3)
        case 4:
            b4 = bullet(t.b4, 200, 4)
        case 5:
            b5 = bullet(t.b5, 200, 5)

def fire_bullet():
    b=0
    for i in range(1,6):
        select = bullets[i]
        if select == 1:
            match i:
                case 1:
                    b1.fire()
                case 2:
                    b2.fire()
                case 3:
                    b3.fire()
                case 4:
                    b4.fire()
                case 5:
                    b5.fire()


bullet_timeout = 1


ship_controller = body("player", t.ship)
ship_speed = 0
ship_heading = 0
new_ship_heading = 0
pressed = 0
while True:
    t.s.tracer(0)
    pressed = 0
    if k.is_pressed("w"):
        ship_heading = t.ship.heading()
        pressed = 1
        if ship_speed < 75:
            ship_speed += 5
    elif ship_speed != 0:
        ship_speed -= 1
    if k.is_pressed("a"):
        t.ship.left(10)
        if pressed == 1:
            ship_heading = t.ship.heading()
    if k.is_pressed("d"):
        t.ship.right(10)
        if pressed == 1:
            ship_heading = t.ship.heading()
    if k.is_pressed("space"):
        if bullet_timeout == 0:
            spawn_bullet()
            bullet_timeout = 10
    if bullet_timeout != 0:
        bullet_timeout -= 1    
    

    fire_bullet()
    ship_controller.switch_sides()
    new_ship_heading = t.ship.heading()
    t.ship.seth(ship_heading)
    t.ship.forward(ship_speed/10)
    t.ship.seth(new_ship_heading)


    if k.is_pressed("esc"):
        break
    t.s.tracer(1)
    ti.sleep(0.05)

exit()
t.s.done()