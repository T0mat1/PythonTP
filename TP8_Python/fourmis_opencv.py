# -*- coding: utf-8 -*-
# author: Thomas Rossi
from threading import Thread

import numpy as np
import cv2
import random as rand

# opencv color format is BGR
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

# Ants configurations
CONFIG_1 = 1
CONFIG_2 = 2

# Ants directions
DIRECTIONS = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]


class AppFourmis:

    def __init__(self, nb_fourmis=1):
        self.window_name = ""
        self.height = 600
        self.width = 600
        self.image = np.zeros((self.height, self.width, 3), np.uint8)
        self.image[:] = WHITE
        self.running = False
        self.nb_fourmis = nb_fourmis

    def update(self):
        while self.running:
            cv2.imshow(self.window_name, self.image)
            if cv2.waitKey(1) == ord('a'):
                self.stop()

    def destroy(self):
        cv2.destroyAllWindows()

    def set_color(self, x, y, color):
        self.image[x, y] = color

    def start(self):
        self.running = True
        self.update()

    def stop(self):
        self.running = False
        self.destroy()

    class Fourmi(Thread):

        def __init__(self, color, fcolor, config=CONFIG_1, proba=(1 / 3, 1 / 3, 1 / 3), proba_color=0, init_x=0, init_y=0, facing=2):
            super().__init__()
            self.x = init_x
            self.y = init_y
            self.color = color
            self.followed_color = fcolor
            self.config = config
            self.proba = proba
            self.proba_color = proba_color
            self.facing_direction = facing

        def turn_left(self):
            self.facing_direction -= self.config
            if self.facing_direction < 0:
                self.facing_direction += 8
            self.x, self.y = self.x + DIRECTIONS[self.facing_direction][0], self.y + DIRECTIONS[self.facing_direction][1]

        def turn_right(self):
            self.facing_direction += self.config
            if self.facing_direction > 7:
                self.facing_direction -= 8
            self.x, self.y = self.x + DIRECTIONS[self.facing_direction][0], self.y + DIRECTIONS[self.facing_direction][1]

        def move_forward(self):
            self.x, self.y = self.x + DIRECTIONS[self.facing_direction][0], self.y + DIRECTIONS[self.facing_direction][1]


if __name__ == "__main__":
    app = AppFourmis()
    app.start()
