# -*- coding: utf-8 -*-
# author: Thomas Rossi
import time
from threading import Thread

import numpy as np
import cv2
import random as rand

# opencv color format is BGR
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (127, 127, 127)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
BROWN = (19, 69, 139)
PINK = (147, 20, 255)
PURPLE = (130, 0, 75)
ORANGE = (0, 69, 255)
CYAN = (255, 255, 0)

COLORS = [WHITE, BLACK, RED, GREEN, BLUE, YELLOW, BROWN, PINK, PURPLE, ORANGE, GREY, CYAN]

# Ants configurations
CONFIG_1 = 1
CONFIG_2 = 2

# Ants directions
DIRECTIONS = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]


class AppFourmis:

    def __init__(self, nb_fourmis=4):
        self.window_name = "Painting ants"
        self.height = 600
        self.width = 600
        self.image = np.zeros((self.height, self.width, 3), np.uint8)
        self.image[:] = WHITE
        self.running = False
        self.nb_fourmis = nb_fourmis
        self.fourmis = []

    def update(self):
        while self.running:
            cv2.imshow(self.window_name, self.image)
            if cv2.waitKey(1) == ord('a'):
                self.stop()

    def destroy(self):
        cv2.destroyAllWindows()

    def start(self):
        for i in range(self.nb_fourmis):
            x, y = rand.randint(0, self.width-1), rand.randint(0, self.height-1)
            self.fourmis.append(Fourmi(image=self.image, color=COLORS[1+i], x=x, y=y, facing=rand.randint(0, 7)))
            self.fourmis[i].start()
        self.running = True
        self.update()

    def stop(self):
        self.running = False
        for ant in self.fourmis:
            ant.is_running = False
            ant.join()
        self.destroy()


class Fourmi(Thread):

    def __init__(self, image, color, fcolor=WHITE, lum_threshold=40, config=CONFIG_1, proba=(1 / 3, 1 / 3, 1 / 3), proba_color=0, x=0, y=0, num_iteration=100000, facing=2):
        assert int(proba[0]+proba[1]+proba[2]) == 1, "Le vecteur de probabilités doit être stochastique"
        super().__init__()
        self.image = image
        self.x = x
        self.y = y
        self.color = color
        self.followed_color = fcolor
        self.lum_threshold = lum_threshold
        self.config = config
        self.proba = proba
        self.proba_color = proba_color
        self.facing_direction = facing
        self.num_iteration = num_iteration
        self.is_running = True
        self.set_color()

    def luminance(self, color):
        return 0.2426 * color[2] + 0.7152 * color[1] + 0.0722 * color[0]

    def set_color(self):
        self.image[self.x, self.y] = self.color

    def turn_left(self):
        self.facing_direction -= self.config
        if self.facing_direction < 0:
            self.facing_direction += 8
        self.compute_positions()

    def turn_right(self):
        self.facing_direction += self.config
        if self.facing_direction > 7:
            self.facing_direction -= 8
        self.compute_positions()

    def move_forward(self):
        self.compute_positions()

    def compute_positions(self):
        self.x, self.y = (self.x + DIRECTIONS[self.facing_direction][0]) % (self.image.shape[0] - 1), \
                         (self.y + DIRECTIONS[self.facing_direction][1]) % (self.image.shape[1] - 1)

    def move(self):
        r = rand.random()
        if r <= self.proba[0]:
            self.turn_left()
        elif r <= self.proba[0]+self.proba[1]:
            self.move_forward()
        else:
            self.turn_right()
        self.set_color()

    def run(self):
        for _ in range(self.num_iteration):
            self.move()
            time.sleep(0.005)
            if not self.is_running:
                break


if __name__ == "__main__":
    app = AppFourmis(11)
    app.start()
