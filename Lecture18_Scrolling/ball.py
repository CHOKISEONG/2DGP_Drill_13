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
        self.boy_x, self.boy_y = common.boy.x, common.boy.y

    def draw(self):
        self.image.clip_draw(0,0,23,23,self.x- common.court.window_left, self.y - common.court.window_bottom)

    def update(self):
        pass

    def handle_collision(self, group, other):
        pass