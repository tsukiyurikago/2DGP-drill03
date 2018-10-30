from pico2d import *
import game_world

class Ghost:
    image = None

    def __init__(self, x = 400, y = 300):
        if Ghost.image == None:
            Ghost.image = load_image('ball21x21.png')
        self.x = x
        self.y = y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += 1

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
