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
            self.astroid_position()
            self.turtle.showturtle()

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
    
    def astroid_position(self):
        #position
        w = r.randint(0,3)
        match w:
            case 0:
                x = r.randint(-320, 320)
                y = -240
            case 1:
                x = r.randint(-320, 320)
                y = 240
            case 2:
                x = -320
                y = r.randint(-320, 320)
            case 3:
                x = 320
                y = r.randint(-320, 320)
        
        #rotation
        ang = self.turtle.towards(0,0)
        ang_modifier = r.randint(-20,20)
        self.turtle.seth(ang+ang_modifier)
        self.turtle.goto(x,y)

    def move_astroid(self):
        self.turtle.forward(self.speed)
        self.kill_on_edge()

    def kill_on_edge(self):
        if self.turtle.xcor() >= 320 or self.turtle.xcor() <= -330 or self.turtle.ycor() >= 220 or self.turtle.ycor() <= -230:
            self.kill_instance()

    def collision(self):
        if self.type == "ship":
            for i in range(15):
                if astroids[i] == 1:
                    match i:
                        case 0:
                            print(self.turtle.distance(a0.turtle))
                            if self.turtle.distance(a0.turtle) < 20:
                                self.kill_instance()
                        case 1:
                            if self.turtle.distance(a1.turtle) < 20:
                                self.kill_instance()    
                        case 2:
                            if self.turtle.distance(a2.turtle) < 20:
                                self.kill_instance()
                        case 3:
                            if self.turtle.distance(a3.turtle) < 20:
                                self.kill_instance()
                        case 4:
                            if self.turtle.distance(a4.turtle) < 20:
                                self.kill_instance()
                        case 5:
                            if self.turtle.distance(a5.turtle) < 20:
                                self.kill_instance()
                        case 6:
                            if self.turtle.distance(a6.turtle) < 20:
                                self.kill_instance()
                        case 7:
                            if self.turtle.distance(a7.turtle) < 20:
                                self.kill_instance()
                        case 8:
                            if self.turtle.distance(a8.turtle) < 20:
                                self.kill_instance()
                        case 9:
                            if self.turtle.distance(a9.turtle) < 20:
                                self.kill_instance()
                        case 10:
                            if self.turtle.distance(a10.turtle) < 20:
                                self.kill_instance()
                        case 11:
                            if self.turtle.distance(a11.turtle) < 20:
                                self.kill_instance()
                        case 12:
                            if self.turtle.distance(a12.turtle) < 20:
                                self.kill_instance()
                        case 13:
                            if self.turtle.distance(a13.turtle) < 20:
                                self.kill_instance()
                        case 14:
                            if self.turtle.distance(a14.turtle) < 20:
                                self.kill_instance()

        elif self.type == "bullet":
            pass

    def kill_instance(self):
        match self.type:
            case "bullet":
                bullets[self.instance] = 0
                self.turtle.hideturtle()
            case "ship":
                self.turtle
            case "astroid":
                astroids[self.instance] = 0
                self.turtle.hideturtle()
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
    shape = False
    for i in range(15):
        select = astroids[i]
        if select == 0:
            a = i
            astroids[i] = 1
            break
    i = r.randint(0,10)
    if i == 0:
        i = r.randint(0,2)
        match i:
            case 0:
                shape = "assets/gif/sa0.gif"
            case 1:
                shape = "assets/gif/sa1.gif"
            case 2:
                shape = "assets/gif/sa2.gif"
    else:
        i = r.randint(0,2)
        match i:
            case 0:
                shape = "assets/gif/ba0.gif"
            case 1:
                shape = "assets/gif/ba1.gif"
            case 2:
                shape = "assets/gif/ba2.gif"
    speed = r.randint(3,7)

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
            
def move_astroid():
    for i in range(15):
        if astroids[i] == 1:
            match i:
                case 0:
                    a0.move_astroid()
                case 1:
                    a1.move_astroid()
                case 2:
                    a2.move_astroid()
                case 3:
                    a3.move_astroid()
                case 4:
                    a4.move_astroid()
                case 5:
                    a5.move_astroid()
                case 6:
                    a6.move_astroid()
                case 7:
                    a7.move_astroid()
                case 8:
                    a8.move_astroid()
                case 9:
                    a9.move_astroid()
                case 10:
                    a10.move_astroid()
                case 11:
                    a11.move_astroid()
                case 12:
                    a12.move_astroid()
                case 13:
                    a13.move_astroid()
                case 14:
                    a14.move_astroid()


ship_controller = body(t.ship, "ship", 0)
ship_speed = 0
ship_heading = 0
new_ship_heading = 0
pressed = 0
bullet_timeout = 0
test = 1

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
    #astroid spawning 
    spawn_chance = r.randint(0,10)  
    if spawn_chance == 0:
        spawn_astroid()
    

    move_astroid()
    fire_bullet()
    ship_controller.collision()
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