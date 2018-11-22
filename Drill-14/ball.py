import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1837), random.randint(0, 1109), 0
        self.type = 2
        self.cx = 0.0
        self.cy = 0.0

    def get_bb(self):
        # fill here
        return self.cx - 10, self.cy - 10, self.cx + 10, self.cy + 10

    def draw(self):
        self.image.draw(self.cx, self.cy)
        # fill here
        draw_rectangle(*self.get_bb())

    def set_center_object(self, boy):
        self.center_object = boy

    def update(self):
#        self.cx,self.cy = self.x - self.center_object.x + (self.canvas_width//2), self.y - self.center_object.y + (self.canvas_height//2)
        self.cx,self.cy = self.x - self.center_object.bg.window_left, self.y - self.center_object.bg.window_bottom
        self.y -= self.fall_speed * game_framework.frame_time

    def stop(self):
        self.fall_speed = 0



class BigBall(Ball):
    MIN_FALL_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200 # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 500, random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

