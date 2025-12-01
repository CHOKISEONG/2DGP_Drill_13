from pico2d import *
from random import randrange
import common
import game_world

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y= randrange(0, common.court.w), randrange(0, common.court.h)
        print(common.court.w)
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def handle_collision(self, group, other):
        pass