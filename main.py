import t_config as t
import time as ti
import keyboard as k
import random as r

class body:
    def __init__(self, turtle, type, instance, range=False, speed = False):
        self.type = type
        self.turtle = turtle
        self.instance = instance
        if self.type == "bullet":
            self.range = range
            self.turtle.showturtle()
            self.turtle.goto(t.ship.xcor(), t.ship.ycor())
            self.turtle.setheading(t.ship.heading())
        if self.type == "astroid":
            self.speed = speed

    def switch_sides(self):
        if self.turtle.xcor() >= 320:
            self.turtle.setpos(-320, self.turtle.ycor())
        elif self.turtle.xcor() <= -330:
            self.turtle.setpos(310, self.turtle.ycor())
        if self.turtle.ycor() >= 220:
            self.turtle.setpos(self.turtle.xcor(), -230)
        elif self.turtle.ycor() <= -230:
            self.turtle.setpos(self.turtle.xcor(), 220)

    def bullet_fire(self):
        self.range -= 10
        self.turtle.forward(15)
        if self.range <= 0:
            self.kill_instance()
    
    def move_astroid(self):
        
        self.kill_on_edge()

    def kill_on_edge(self):
        if self.turtle.xcor() >= 320 or self.turtle.xcor() <= -330 or self.turtle.ycor() >= 220 or self.turtle.ycor() <= -230:
            self.kill_instance()

    def kill_instance(self):
        match self.type:
            case "bullet":
                bullets[self.instance] = 0
                self.turtle.hideturtle()
            case "ship":
                pass
            case "astroid":
                pass
        del self


bullets = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0
}

astroids = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0,
    12:0,
    13:0,
    14:0
}

def spawn_bullet():
    global b0,b1,b2,b3,b4
    b=0
    for i in range(5):
        select = bullets[i]
        if select == 0:
            b = i
            bullets[i] = 1
            break
    match b:
        case 0:
            b0 = body(t.b0, "bullet", 0, 200)
        case 1:
            b1 = body(t.b1, "bullet", 1, 200)
        case 2:
            b2 = body(t.b2, "bullet", 2, 200)
        case 3:
            b3 = body(t.b3, "bullet", 3, 200)
        case 4:
            b4 = body(t.b4, "bullet", 4, 200)

def fire_bullet():
    for i in range(5):
        if bullets[i] == 1:
            match i:
                case 0:
                    b0.bullet_fire()
                case 1:
                    b1.bullet_fire()
                case 2:
                    b2.bullet_fire()
                case 3:
                    b3.bullet_fire()
                case 4:
                    b4.bullet_fire()

def spawn_astroid():
    global a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14
    a=0
    for i in range(15):
        select = astroids[i]
        if select == 0:
            a = i
            astroids[i] = 1
            break
    if r.randint(0,10) == 0:
        if i == 0:
            for i in range(3):
                match i:
                    case 0:
                        shape = "assets/gif/sa0"
                    case 1:
                        shape = "assets/gif/sa1"
                    case 2:
                        shape = "assets/gif/sa2"
        else:
            for i in range(3):
                match i:
                    case 0:
                        shape = "assets/gif/ba0"
                    case 1:
                        shape = "assets/gif/ba1"
                    case 2:
                        shape = "assets/gif/ba2" 
    speed = r.randint(1,5)

    match a:
        case 0:
            t.a0.shape(shape)
            a0 = body(t.a0, "astroid", 0, speed = speed)
        case 1:
            t.a1.shape(shape)
            a1 = body(t.a1, "astroid", 1, speed = speed)
        case 2:
            t.a2.shape(shape)
            a2 = body(t.a2, "astroid", 2, speed = speed)
        case 3:
            t.a3.shape(shape)
            a3 = body(t.a3, "astroid", 3, speed = speed)
        case 4:
            t.a4.shape(shape)
            a4 = body(t.a4, "astroid", 4, speed = speed)
        case 5:
            t.a5.shape(shape)
            a5 = body(t.a5, "astroid", 5, speed = speed)
        case 6:
            t.a6.shape(shape)
            a6 = body(t.a6, "astroid", 6, speed = speed)
        case 7:
            t.a7.shape(shape)
            a7 = body(t.a7, "astroid", 7, speed = speed)
        case 8:
            t.a8.shape(shape)
            a8 = body(t.a8, "astroid", 8, speed = speed)
        case 9:
            t.a9.shape(shape)
            a9 = body(t.a9, "astroid", 9, speed = speed)
        case 10:
            t.a10.shape(shape)
            a10 = body(t.a10, "astroid", 10, speed = speed)
        case 11:
            t.a11.shape(shape)
            a11 = body(t.a11, "astroid", 11, speed = speed)
        case 12:
            t.a12.shape(shape)
            a12 = body(t.a12, "astroid", 12, speed = speed)
        case 13:
            t.a13.shape(shape)
            a13 = body(t.a13, "astroid", 13, speed = speed)
        case 14:
            t.a14.shape(shape)
            a14 = body(t.a14, "astroid", 14, speed = speed)
            


bullet_timeout = 1

ship_controller = body(t.ship, "ship", 0)
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