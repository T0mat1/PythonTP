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
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)

COLORS = [WHITE, BLACK, RED, GREEN, BLUE, YELLOW]

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
            self.fourmis.append(Fourmi(image=self.image, color=COLORS[1+i], x=i*100, y=300))
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

    def __init__(self, image, color, fcolor=WHITE, luminance_diff=40, config=CONFIG_1, proba=(1 / 3, 1 / 3, 1 / 3), proba_color=0, x=0, y=0, facing=2):
        super().__init__()
        self.image = image
        self.x = x
        self.y = y
        self.color = color
        self.followed_color = fcolor
        self.lum_diff = luminance_diff
        self.config = config
        self.proba = proba
        self.proba_color = proba_color
        self.facing_direction = facing
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
        r = rand.randint(0, 2)
        if r == 0:
            self.turn_left()
        if r == 1:
            self.move_forward()
        if r == 2:
            self.turn_right()
        if self.x >= 600 or self.y >= 600:
            print((self.x, self.y))
        self.set_color()

    def run(self):
        for _ in range(100000):
            self.move()
            time.sleep(0.005)
            if not self.is_running:
                break


if __name__ == "__main__":
    app = AppFourmis(5)
    app.start()
