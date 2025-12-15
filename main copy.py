import t_config as t
import time as ti
import keyboard as k
import random as r

class body:
    def __init__(self, turtle, type, instance, range=False, speed = False, shape=False, size = False, position = False, heading=False, owner=False, lives=False):
        self.type = type
        self.turtle = turtle
        self.instance = instance
        if self.type == "ship":
            self.lives = lives
        if self.type == "bullet":
            self.range = range
            self.owner=owner
            match owner:
                case "ship":
                    self.turtle.goto(t.ship.xcor(), t.ship.ycor())
                    self.turtle.setheading(t.ship.heading())
                case "alien":
                    self.turtle.goto(t.alien.xcor(), t.alien.ycor())
                    self.turtle.seth(self.turtle.towards(ship.turtle))
            self.turtle.showturtle()
        if self.type == "astroid":
            self.speed = speed
            self.size = size
            self.shape = shape
            self.position = position
            self.heading = heading
            self.astroid_position()
            self.turtle.shape(shape)
            self.turtle.showturtle()
        if self.type == "alien":
            self.speed = speed
            self.turtle.goto(position)
            self.turtle.seth(heading)
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
    
    def astroid_position(self):
        if self.position == False:
        # position
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
            self.turtle.seth(ang)
            self.turtle.goto(x,y)
        else:
            self.turtle.goto(self.position)
            self.turtle.seth(self.heading)

    def bullet_fire(self):
        self.range -= 10
        self.turtle.forward(15)
        if self.range <= 0:
            self.kill_instance()

    def shoot_at_player(self):
        spawn_bullet("alien")


    def move_bodies(self):
        self.turtle.forward(self.speed)
        self.kill_on_edge()

    def kill_on_edge(self):
        if self.turtle.xcor() >= 350 or self.turtle.xcor() <= -350 or self.turtle.ycor() >= 250 or self.turtle.ycor() <= -250:
            self.kill_instance()

    def collision(self):
        if self.type == "ship":
            for i in range(15):
                if astroids[i]:
                    match i:
                        case 0:
                            if a0.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30 
                            if self.turtle.distance(a0.turtle) < hitbox:
                                self.ship_die()
                        case 1:
                            if a1.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a1.turtle) < hitbox:
                                self.ship_die() 
                        case 2:
                            if a2.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a2.turtle) < hitbox:
                                self.ship_die()
                        case 3:
                            if a3.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a3.turtle) < hitbox:
                                self.ship_die()
                        case 4:
                            if a4.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a4.turtle) < hitbox:
                                self.ship_die()
                        case 5:
                            if a5.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a5.turtle) < hitbox:
                                self.ship_die()
                        case 6:
                            if a6.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a6.turtle) < hitbox:
                                self.ship_die()
                        case 7:
                            if a7.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a7.turtle) < hitbox:
                                self.ship_die()
                        case 8:
                            if a8.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a8.turtle) < hitbox:
                               self.ship_die()
                        case 9:
                            if a9.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a9.turtle) < hitbox:
                                self.ship_die()
                        case 10:
                            if a10.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a10.turtle) < hitbox:
                                self.ship_die()
                        case 11:
                            if a11.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a11.turtle) < hitbox:
                                self.ship_die()
                        case 12:
                            if a12.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a12.turtle) < hitbox:
                                self.ship_die()
                        case 13:
                            if a13.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a13.turtle) < hitbox:
                                self.ship_die()
                        case 14:
                            if a14.size == 0:
                                hitbox = 60
                            else:
                                hitbox = 30
                            if self.turtle.distance(a14.turtle) < hitbox:
                                self.ship_die()

        elif self.type == "bullet":
            for i in range(15):
                if astroids[i]:
                    match i:
                        case 0:
                            if self.turtle.distance(a0.turtle) < 60:
                                if a0.size == 0:
                                    respawn_astroid(a0.speed, a0.shape, a0.size, a0.turtle.pos(), a0.turtle.heading())
                                    ti.sleep(0.05)
                                a0.kill_instance()
                                self.kill_instance()
                        case 1:
                            if self.turtle.distance(a1.turtle) < 60:
                                if a1.size == 0:
                                    respawn_astroid(a1.speed, a1.shape, a1.size, a1.turtle.pos(), a1.turtle.heading())
                                    ti.sleep(0.05)
                                a1.kill_instance()
                                self.kill_instance()
                        case 2:
                            if self.turtle.distance(a2.turtle) < 60:
                                if a2.size == 0:
                                    respawn_astroid(a2.speed, a2.shape, a2.size, a2.turtle.pos(), a2.turtle.heading())
                                    ti.sleep(0.05)
                                a2.kill_instance()
                                self.kill_instance()
                        case 3:
                            if self.turtle.distance(a3.turtle) < 60:
                                if a3.size == 0:
                                    respawn_astroid(a3.speed, a3.shape, a3.size, a3.turtle.pos(), a3.turtle.heading())
                                    ti.sleep(0.05)
                                a3.kill_instance()
                                self.kill_instance()
                        case 4:
                            if self.turtle.distance(a4.turtle) < 60:
                                if a4.size == 0:
                                    respawn_astroid(a4.speed, a4.shape, a4.size, a4.turtle.pos(), a4.turtle.heading())
                                    ti.sleep(0.05)
                                a4.kill_instance()
                                self.kill_instance()
                        case 5:
                            if self.turtle.distance(a5.turtle) < 60:
                                if a5.size == 0:
                                    respawn_astroid(a5.speed, a5.shape, a5.size, a5.turtle.pos(), a5.turtle.heading())
                                    ti.sleep(0.05)
                                a5.kill_instance()
                                self.kill_instance()
                        case 6:
                            if self.turtle.distance(a6.turtle) < 60:
                                if a6.size == 0:
                                    respawn_astroid(a6.speed, a6.shape, a6.size, a6.turtle.pos(), a6.turtle.heading())
                                    ti.sleep(0.05)
                                a6.kill_instance()
                                self.kill_instance()
                        case 7:
                            if self.turtle.distance(a7.turtle) < 60:
                                if a7.size == 0:
                                    respawn_astroid(a7.speed, a7.shape, a7.size, a7.turtle.pos(), a7.turtle.heading())
                                    ti.sleep(0.05)
                                a7.kill_instance()
                                self.kill_instance()
                        case 8:
                            if self.turtle.distance(a8.turtle) < 60:
                                if a8.size == 0:
                                    respawn_astroid(a8.speed, a8.shape, a8.size, a8.turtle.pos(), a8.turtle.heading())
                                    ti.sleep(0.05)
                                a8.kill_instance()
                                self.kill_instance()
                        case 9:
                            if self.turtle.distance(a9.turtle) < 60:
                                if a9.size == 0:
                                    respawn_astroid(a9.speed, a9.shape, a9.size, a9.turtle.pos(), a9.turtle.heading())
                                    ti.sleep(0.05)
                                a9.kill_instance()
                                self.kill_instance()
                        case 10:
                            if self.turtle.distance(a10.turtle) < 60:
                                if a10.size == 0:
                                    respawn_astroid(a10.speed, a10.shape, a10.size, a10.turtle.pos(), a10.turtle.heading())
                                    ti.sleep(0.05)
                                a10.kill_instance()
                                self.kill_instance()
                        case 11:
                            if self.turtle.distance(a11.turtle) < 60:
                                if a11.size == 0:
                                    respawn_astroid(a11.speed, a11.shape, a11.size, a11.turtle.pos(), a11.turtle.heading())
                                    ti.sleep(0.05)
                                a11.kill_instance()
                                self.kill_instance()
                        case 12:
                            if self.turtle.distance(a12.turtle) < 60:
                                if a12.size == 0:
                                    respawn_astroid(a12.speed, a12.shape, a12.size, a12.turtle.pos(), a12.turtle.heading())
                                    ti.sleep(0.05)
                                a12.kill_instance()
                                self.kill_instance()
                        case 13:
                            if self.turtle.distance(a13.turtle) < 60:
                                if a13.size == 0:
                                    respawn_astroid(a13.speed, a13.shape, a13.size, a13.turtle.pos(), a13.turtle.heading())
                                    ti.sleep(0.05)
                                a13.kill_instance()
                                self.kill_instance()
                        case 14:
                            if self.turtle.distance(a14.turtle) < 60:
                                if a14.size == 0:
                                    respawn_astroid(a14.speed, a14.shape, a14.size, a14.turtle.pos(), a14.turtle.heading())
                                    ti.sleep(0.05)
                                a14.kill_instance()
                                self.kill_instance()

            if self.owner == "alien":
                if self.turtle.distance(ship.turtle) < 30: 
                    self.kill_instance()
                    ti.sleep(0.01)
                    ship.ship_die()
            elif self.owner == "ship":
                if aliens[0] == 1:
                    if self.turtle.distance(alien.turtle) < 40:
                        alien.kill_instance()
                        self.kill_instance()
            
# ...existing code...
    def reset(self):
        # remove any active bullet instances (b0..b4) and mark slots free
        for i in range(5):
            if bullets.get(i):
                bullets[i] = 0
                varname = f"b{i}"
                inst = globals().get(varname)
                if inst:
                    try:
                        inst.kill_instance()
                    except Exception:
                        try:
                            inst.turtle.hideturtle()
                        except Exception:
                            pass
                    globals().pop(varname, None)
        
        for i in range(15):
            if astroids.get(i):
                astroids[i] = 0
                varname = f"a{i}"
                inst = globals().get(varname)
                if inst:
                    try:
                        inst.kill_instance()
                    except Exception:
                        try:
                            inst.turtle.hideturtle()
                        except Exception:
                            pass
                    globals().pop(varname, None)

        if aliens.get(0):
            aliens[i] = 0
            varname = "alien"
            inst = globals().get(varname)
            if inst:
                try:
                    inst.kill_instance()
                except Exception:
                    try:
                        inst.turtle.hideturtle()
                    except Exception:
                        pass
                globals().pop(varname, None)
                 
    def ship_die(self):
        global state
        self.turtle.hideturtle()
        self.lives -= 1
        if self.lives == 0:
            state = 4
        else:
            self.reset()
            state = 2

    def kill_instance(self):
        match self.type:
            case "bullet":
                bullets[self.instance] = 0
                self.turtle.hideturtle()
            case "astroid":
                astroids[self.instance] = 0
                self.turtle.hideturtle()
            case "alien":
                aliens[self.instance] = 0
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

aliens = {
    0:0
}

def spawn_bullet(owner):
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
            b0 = body(t.b0, "bullet", 0, 200, owner=owner)
        case 1:
            b1 = body(t.b1, "bullet", 1, 200, owner=owner)
        case 2:
            b2 = body(t.b2, "bullet", 2, 200, owner=owner)
        case 3:
            b3 = body(t.b3, "bullet", 3, 200, owner=owner)
        case 4:
            b4 = body(t.b4, "bullet", 4, 200, owner=owner)

def fire_bullet():
    for i in range(5):
        if bullets[i] == 1:
            match i:
                case 0:
                    b0.bullet_fire()
                    b0.collision()
                case 1:
                    b1.bullet_fire()
                    b1.collision()
                case 2:
                    b2.bullet_fire()
                    b2.collision()
                case 3:
                    b3.bullet_fire()
                    b3.collision()
                case 4:
                    b4.bullet_fire()
                    b4.collision()

def spawn_astroid():
    global a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14
    a=0
    shape = False
    size = 0
    for i in range(15):
        select = astroids[i]
        if select == 0:
            a = i
            astroids[i] = 1
            break
    i = r.randint(0,10)
    if i == 0:
        size = 1
        i = r.randint(0,2)
        match i:
            case 0:
                shape = "assets/sa0.gif"
            case 1:
                shape = "assets/sa1.gif"
            case 2:
                shape = "assets/sa2.gif"
    else:
        size = 0
        i = r.randint(0,2)
        match i:
            case 0:
                shape = "assets/ba0.gif"
            case 1:
                shape = "assets/ba1.gif"
            case 2:
                shape = "assets/ba2.gif"
    speed = r.randint(3,7)

    match a:
        case 0:
            a0 = body(t.a0, "astroid", 0, speed = speed, shape=shape, size = size)
        case 1:
            a1 = body(t.a1, "astroid", 1, speed = speed, shape=shape, size = size)
        case 2:
            a2 = body(t.a2, "astroid", 2, speed = speed, shape=shape, size = size)
        case 3:
            a3 = body(t.a3, "astroid", 3, speed = speed, shape=shape, size = size)
        case 4:
            a4 = body(t.a4, "astroid", 4, speed = speed, shape=shape, size = size)
        case 5:
            a5 = body(t.a5, "astroid", 5, speed = speed, shape=shape, size = size)
        case 6:
            a6 = body(t.a6, "astroid", 6, speed = speed, shape=shape, size = size)
        case 7:
            a7 = body(t.a7, "astroid", 7, speed = speed, shape=shape, size = size)
        case 8:
            a8 = body(t.a8, "astroid", 8, speed = speed, shape=shape, size = size)
        case 9:
            a9 = body(t.a9, "astroid", 9, speed = speed, shape=shape, size = size)
        case 10:
            a10 = body(t.a10, "astroid", 10, speed = speed, shape=shape, size = size)
        case 11:
            a11 = body(t.a11, "astroid", 11, speed = speed, shape=shape, size = size)
        case 12:
            a12 = body(t.a12, "astroid", 12, speed = speed, shape=shape, size = size)
        case 13:
            a13 = body(t.a13, "astroid", 13, speed = speed, shape=shape, size = size)
        case 14:
            a14 = body(t.a14, "astroid", 14, speed = speed, shape=shape, size = size)

def respawn_astroid(speed, shape, size, position, heading):
    global a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14
    a = 0
    for i in range(15):
        select = astroids[i]
        if select == 0:
            a = i
            astroids[i] = 1
            break
    match shape:
        case "assets/ba0.gif":
            shape = "assets/sa0.gif"
        case "assets/ba1.gif":
            shape = "assets/sa1.gif"
        case "assets/ba2.gif":
            shape = "assets/sa2.gif"
    match a:
        case 0:
            a0 = body(t.a0, "astroid", 0, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 1:
            a1 = body(t.a1, "astroid", 1, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 2:
            a2 = body(t.a2, "astroid", 2, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 3:
            a3 = body(t.a3, "astroid", 3, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 4:
            a4 = body(t.a4, "astroid", 4, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 5:
            a5 = body(t.a5, "astroid", 5, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 6:
            a6 = body(t.a6, "astroid", 6, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 7:
            a7 = body(t.a7, "astroid", 7, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 8:
            a8 = body(t.a8, "astroid", 8, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 9:
            a9 = body(t.a9, "astroid", 9, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 10:
            a10 = body(t.a10, "astroid", 10, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 11:
            a11 = body(t.a11, "astroid", 11, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 12:
            a12 = body(t.a12, "astroid", 12, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 13:
            a13 = body(t.a13, "astroid", 13, speed = speed, shape=shape, size = size+1, position=position, heading=heading)
        case 14:
            a14 = body(t.a14, "astroid", 14, speed = speed, shape=shape, size = size+1, position=position, heading=heading)


def move_astroid():
    for i in range(15):
        if astroids[i] == 1:
            match i:
                case 0:
                    a0.move_bodies()
                case 1:
                    a1.move_bodies()
                case 2:
                    a2.move_bodies()
                case 3:
                    a3.move_bodies()
                case 4:
                    a4.move_bodies()
                case 5:
                    a5.move_bodies()
                case 6:
                    a6.move_bodies()
                case 7:
                    a7.move_bodies()
                case 8:
                    a8.move_bodies()
                case 9:
                    a9.move_bodies()
                case 10:
                    a10.move_bodies()
                case 11:
                    a11.move_bodies()
                case 12:
                    a12.move_bodies()
                case 13:
                    a13.move_bodies()
                case 14:
                    a14.move_bodies()

def spawn_alien():
    global alien
    # speed, heading, position
    x, y = 0,0
    pos = r.randint(0,1)
    match pos:
        case 0:
            heading = 0
            x = -340
        case 1:
            heading = 180
            x = 340               
    y = r.randint(-240,240)
    position = (x,y)
    speed = r.randint(5,8)

    alien = body(turtle=t.alien,type="alien",instance=0, speed=speed, position=position, heading=heading)

# 0 - menu, 1 - running, 2 - respawning ship, 3 - quit game
state = 1
ship = body(t.ship, "ship", 0, lives=3)
ship_speed = 0
ship_heading = 0
new_ship_heading = 0
pressed = 0
fired = 0
bullet_timeout = 0



def astroids_mainloop():
    global state, ship, ship_speed, ship_heading, new_ship_heading, pressed, fired, bullet_timeout
    t.s.tracer(0)
    pressed = 0
    if k.is_pressed("w") or k.is_pressed("up"):
        ship_heading = t.ship.heading()
        pressed = 1
        if ship_speed < 75:
            ship_speed += 5
    elif ship_speed != 0:
        ship_speed -= 1
    if k.is_pressed("a") or k.is_pressed("left"):
        t.ship.left(10)
        if pressed == 1:
            ship_heading = t.ship.heading()
    if k.is_pressed("d") or k.is_pressed("right"):
        t.ship.right(10)
        if pressed == 1:
            ship_heading = t.ship.heading()
    if k.is_pressed("space"):
        if bullet_timeout == 0 and fired == 0:
            spawn_bullet("ship")
            bullet_timeout = 6
            fired = 1
    if bullet_timeout != 0:
        bullet_timeout -= 1
    if k.is_pressed("space") == False:
        fired = 0

    #astroid spawning   
    if r.randint(0,15) == 0:
        spawn_astroid()

    # alien spawing
    if r.randint(0,20) == 0 and aliens[0] == 0:
        spawn_alien()
        aliens[0] = 1

    move_astroid()
    fire_bullet()
    if aliens[0] == 1:
        alien.move_bodies()
        alien.collision()
        if r.randint(0,25) == 0:
            alien.shoot_at_player()
    ship.collision()
    ship.switch_sides()
    new_ship_heading = t.ship.heading()
    t.ship.seth(ship_heading)
    t.ship.forward(ship_speed/10)
    t.ship.seth(new_ship_heading)

    if k.is_pressed("esc"):
        state = 3
    t.s.tracer(1)
    ti.sleep(0.05)

def respawn_ship():
    global state
    ship.turtle.goto(0,0)
    ship.turtle.seth(0)
    ti.sleep(1)
    ship.turtle.showturtle()
    state = 1

def quit_game():
    exit()
    t.s.done()

while True:
    if state == 1:
        astroids_mainloop()
    elif state == 2:
        respawn_ship()
    elif state == 3:
        quit_game()
    elif state == 4:
        # end screen eventually
        quit_game()