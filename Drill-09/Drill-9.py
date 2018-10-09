from pico2d import *
import random

# Game object class here
class m_ball:
    def __init__(self):
        self.image1 = load_image('ball21x21.png')
        self.image2 = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 800), 600
        self.yspeed = random.randint(0, 10)
        self.size = random.randint(0, 1)

    def update(self):
        if self.y <= 60:
            self.yspeed = self.yspeed*-0.7
            #self.y -= self.yspeed

        else:
            if self.yspeed < 1 and self.yspeed > -1:
                pass

            else:
                self.y -= self.yspeed

        if self.yspeed<20.0:
            self.yspeed = self.yspeed + 0.1

    def draw(self):
        if self.size == 0:
            self.image1.draw(self.x, self.y)
        else:
            self.image2.draw(self.x, self.y)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

m_balls = [m_ball() for i in range(20)]

team = [Boy() for i in range(11)]
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()

    for ball in m_balls:
        ball.update()

    for object in team:
        object.update()

    clear_canvas()
    grass.draw()
    for ball in m_balls:
        ball.draw()

    for object in team:
        object.draw()
    update_canvas()

    delay(0.016)
# finalization code
close_canvas()