import pygame as pg
import Constants as const

class Graphics:
    def __init__(self):
        self.win = pg.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))
        pg.display.set_caption("You VS x kids")

    def update_window(self, player, enemies):
        self.win.fill((4, 233, 195))

        # need to change for images
        pg.draw.rect(self.win, (0, 0, 255), pg.Rect(player.x_pos, player.y_pos, 10, 20))
        for enemy in enemies:
            pg.draw.rect(self.win, (255, 0, 0), pg.Rect(enemy.x_pos, enemy.y_pos, 10, 20))

        pg.display.update()
        #print("updated")


'''
# ==========
#  FUNCTIONS
# ==========

def signed_distance_to_line(m, b, x, y):
    """Signed distance from (x,y) to the line y = m*x + b.
    Positive when the point is on the half-space y >= m*x + b ("below" the line on screen).
    """
    return (y - (m * x + b)) / math.sqrt(m * m + 1)

def line_normal_down(m):
    """Unit normal that points toward increasing screen-y (down)."""
    nx, ny = -m, 1.0
    inv = math.hypot(nx, ny)
    return nx / inv, ny / inv

def closest_point_on_line(m, b, x, y):
    # Formula for closest x on the line y = m*x + b, then y from the line
    x_closest = (x + m * (y - b)) / (m ** 2 + 1)
    y_closest = m * x_closest + b
    return x_closest, y_closest

def bounce(v, m, restitution=0.8, friction=0.9):
    """Reflect velocity v off a line with slope m.
    Uses vector reflection with separate normal (restitution) and tangential (friction) scaling.
    """
    # Normal pointing down; direction does not matter for reflection result
    nx, ny = line_normal_down(m)

    # Decompose into normal and tangential components
    vn = v[0] * nx + v[1] * ny            # scalar normal component
    vt_x = v[0] - vn * nx                 # tangential component (vector)
    vt_y = v[1] - vn * ny

    # Reflect normal, damp both
    vn = -restitution * vn
    vt_x *= friction
    vt_y *= friction

    # Recompose
    return [vn * nx + vt_x, vn * ny + vt_y]

def distance(x, y):
    return math.hypot(x, y)

def is_button_pressed(x_cord, y_cord, width, length):
    return (width + x_cord > x_mouse > x_cord) and (length + y_cord > y_mouse > y_cord) and pg.mouse.get_pressed()

def calculate_velocity_with_radii(bumper_x, bumper_y, total_speed, x_ball, y_ball):
    # Vector from bumper -> ball
    dx = x_ball - bumper_x
    dy = y_ball - bumper_y
    dist = distance(dx, dy)
    if dist == 0:
        # Avoid division by zero; pick an arbitrary direction (to the right)
        return [total_speed, 0.0]
    nx = dx / dist
    ny = dy / dist
    return [nx * total_speed, ny * total_speed]

def draw_window():
    win.fill((4, 233, 195))

def draw_frame():
    draw_window()
    Ball.draw()
    for draw_bumper in regular_bumpers_cords:
        draw_bumper.draw()
    pg.display.update()

def is_key_press(key):
    return old_keys[key] != keys[key] and old_keys[key]



# ==============
#  GAME CLASSES
# ==============
class Ball:

    lives = 3
    alive_balls = []

    def __init__(self, reset_x=40, reset_y=240):  # reset_x = radius + 20, reset_y = HEIGHT / 4
        self.reset_x = reset_x
        self.reset_y = reset_y
        self.radius = 15
        self.color = (255, 220, 75)
        self.velocity = [0.0, 0.0]
        self.x = self.reset_x
        self.y = self.reset_y
        Ball.alive_balls.append(self)

    @staticmethod
    def draw():
        for ball in Ball.alive_balls:
            pg.draw.circle(win, ball.color, (ball.x, ball.y), ball.radius)

    @staticmethod
    def reset():
        Ball.alive_balls = [Ball()]

    @staticmethod
    def restart():
        Ball.alive_balls = []
        Ball.reset()
        Ball.lives = 3
        RegularBumper.restart()


    def destroy_ball(self):
        Ball.alive_balls.remove(self)

    @staticmethod
    def move():
        for ball in Ball.alive_balls:
            ball.x_old = ball.x
            ball.y_old = ball.y
            ball.x += ball.velocity[0] / FPS * 60
            ball.y += ball.velocity[1] / FPS * 60
            # gravity
            ball.velocity[1] += 9.80665 / FPS * 2
            ball.check_collisions()

    @staticmethod
    def add_ball(x, y, velocity):
        Ball()
        Ball.alive_balls[-1].set_position(x, y, velocity)

    def set_position(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity

    @staticmethod
    def get_score():
        return RegularBumper.get_score()

    #check for collisions
    def check_collisions(self):
        self.check_ceiling()
        self.check_floor()
        self.check_right_wall()
        self.check_left_wall()
        self.check_top_angled_wall()
        self.check_bottom_angled_wall()
        self.check_bumpers()

    def check_ceiling(self):
        if self.y < self.radius + 20:  # ceiling
            if debug:
                print("ceiling")
            self.velocity = [self.velocity[0] * 0.9, self.velocity[1] * (-0.8)]
            self.y = self.radius + 20

    def check_floor(self):
        if self.y > HEIGHT - self.radius:
            if len(Ball.alive_balls) == 1:
                Ball.lives -= 1
                self.reset()
                if debug:
                    print(str(Ball.lives) + " lives left")
            else:
                self.destroy_ball()
                if debug:
                    print("destroy ball")

    def check_right_wall(self):
        if self.x > WIDTH - 20 - self.radius:
            if debug:
                print("right wall")
            self.velocity = [self.velocity[0] * (-0.8), self.velocity[1] * 0.9]
            self.x = WIDTH - 20 - self.radius

    def check_left_wall(self):
        if self.x < 20 + self.radius:
            if debug:
                print("left wall")
            self.velocity = [self.velocity[0] * (-0.8), self.velocity[1] * 0.9]
            self.x = 20 + self.radius

    def check_right_small_wall(self):
        if self.x > 120 + self.radius:
            if debug:
                print("right small wall")
            self.velocity = [self.velocity[0] * (-0.8), self.velocity[1] * 0.9]
            self.x = 120 + self.radius

    def check_left_small_wall(self):
        if self.x < 285 - self.radius:
            if debug:
                print("left small wall")
            self.velocity = [self.velocity[0] * (-0.8), self.velocity[1] * 0.9]
            self.x = 285 - self.radius

    def check_top_angled_wall(self):
        # Lines that form TOP boundaries (you collide when you are above them)
        functions = ((1, -250), (-1, 155))
        for m, b in functions:
            dist = signed_distance_to_line(m, b, self.x, self.y)
            nx, ny = line_normal_down(m)  # down normal
            vn = self.velocity[0] * nx + self.velocity[1] * ny
            # If we are within radius "above" the line (d <= 0) and moving upward into it (vn < 0)
            if dist <= self.radius and vn < 0:
                cx, cy = closest_point_on_line(m, b, self.x, self.y)
                eps = 0.5
                # push DOWN away from the top wall
                self.x = cx + nx * (self.radius + eps)
                self.y = cy + ny * (self.radius + eps)
                self.velocity = bounce(self.velocity, m)

    def check_bottom_angled_wall(self):
        # Lines that form BOTTOM boundaries (you collide when you are below them)
        functions = ((3, 250), (-3, 1465))
        for m, b in functions:
            dist = signed_distance_to_line(m, b, self.x, self.y)
            nx, ny = line_normal_down(m)  # down normal
            vn = self.velocity[0] * nx + self.velocity.__getitem__(1) * ny
            # If we are within radius of the line from the bottom side and moving down into it
            if (dist >= -self.radius and vn > 0) and self.y < HEIGHT - self.radius - 95:
                cx, cy = closest_point_on_line(m, b, self.x, self.y)
                eps = 0.5
                # push UP out of the bottom wall (opposite the down normal)
                self.x = cx - nx * (self.radius + eps)
                self.y = cy - ny * (self.radius + eps)
                self.velocity = bounce(self.velocity, m)

    def check_bumpers(self):
        for bumper in regular_bumpers_cords:
            self.velocity = bumper.bump(self.velocity, self.x, self.y, self.radius)


class Bumper:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        pg.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def bump(self, velocity, x_ball, y_ball, radius_ball):
        dx = self.x - x_ball
        dy = self.y - y_ball
        if math.hypot(dx, dy) <= radius_ball + self.radius:
            return calculate_velocity_with_radii(self.x, self.y, math.hypot(velocity[0], velocity[1]) * 1.0, x_ball, y_ball)
        else:
            return [velocity[0], velocity[1]]


class RegularBumper(Bumper):
    __score = 0

    def __init__(self, x, y):
        super().__init__(x, y, 12, (255, 0, 0))

    def bump(self, velocity, x_ball, y_ball, radius_ball):
        dx = self.x - x_ball
        dy = self.y - y_ball
        if math.hypot(dx, dy) <= radius_ball + self.radius:
            RegularBumper.__score += 20
            return calculate_velocity_with_radii(self.x, self.y, math.hypot(velocity[0], velocity[1]) * 1.1, x_ball, y_ball)
        else:
            return [velocity[0], velocity[1]]

    @staticmethod
    def get_score():
        return RegularBumper.__score

    @staticmethod
    def restart():
        RegularBumper.__score = 0

# ===========
#  VARIABLES
# ===========
WIDTH, HEIGHT, window_name = 405, 720, "WorldBall"

win = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
pg.display.set_caption(window_name)

frame = 0
lives = 3
scene_index = 1
FPS = 60

run = True
debug = False

keys = pg.key.get_pressed()
Ball()

# ========
#  MAIN
# ========

time.sleep(3)
while run:
    x_mouse, y_mouse = pg.mouse.get_pos()


    if scene_index == 1:
        regular_bumpers_cords = [
            RegularBumper(WIDTH / 2 - 100, 300),
            RegularBumper(WIDTH / 2 + 100, 300),
            RegularBumper(WIDTH / 2, 450),
        ]
        frame += 1
        time.sleep(1 / FPS)

        # Move balls
        Ball.move()

        # Ball-ball collisions (simple swap demo)
        for i in range(len(Ball.alive_balls)):
            for j in range(i + 1, len(Ball.alive_balls)):
                d_x = Ball.alive_balls[i].x - Ball.alive_balls[j].x
                d_y = Ball.alive_balls[i].y - Ball.alive_balls[j].y
                d = math.hypot(d_x, d_y)
                if Ball.alive_balls[i].radius + Ball.alive_balls[j].radius > d > 0:
                    vi = Ball.alive_balls[i].velocity[:]
                    Ball.alive_balls[i].velocity = Ball.alive_balls[j].velocity[:]
                    Ball.alive_balls[j].velocity = vi

        if Ball.lives == 0:
            run = False

    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            if debug:
                print("quit button")
            run = False

        if event.type == pg.VIDEORESIZE:
            HEIGHT, WIDTH = event.size
            screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
            if debug:
                print("New size:", WIDTH, HEIGHT)

    # Keys
    old_keys = keys
    keys = pg.key.get_pressed()

    if is_key_press(pg.K_SPACE):
        if debug:
            print("space key")
        Ball.restart()

    if is_key_press(pg.K_F3):
        print("F3 key")
        if debug:
            debug = False
            print("debug off")
        else:
            debug = True
            print("debug on")

    if is_key_press(pg.K_ESCAPE):
        print("escape key")
        if scene_index == 1:
            scene_index = 0
        elif scene_index == 0:
            scene_index = 1

    draw_frame()

pg.quit()
print("you're score is: " + str(Ball.get_score()))
exit()
'''