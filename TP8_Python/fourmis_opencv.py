# -*- coding: utf-8 -*-
# author: Thomas Rossi
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


class AppFourmis:

    def __init__(self):
        self.window_name = ""
        self.height = 600
        self.width = 600
        self.image = np.zeros((self.height, self.width, 3), np.uint8)
        self.image[:] = WHITE
        self.running = False

    def update(self):
        while self.running:
            cv2.imshow(self.window_name, self.image)
            if cv2.waitKey(1) == ord('a'):
                self.stop()
            self.paint()

    def destroy(self):
        cv2.destroyAllWindows()

    def set_color(self, x, y, color):
        self.image[x, y] = color

    def paint(self):
        x = rand.randint(0, self.width-1)
        y = rand.randint(0, self.height-1)
        color = (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))
        self.set_color(x, y, color)

    def start(self):
        self.running = True
        self.update()

    def stop(self):
        self.running = False
        self.destroy()

    class Fourmi:

        def __init__(self, color, fcolor, config=CONFIG_1, proba=(1/3, 1/3, 1/3), proba_color=0):
            self.x = 0
            self.y = 0
            self.color = color
            self.followed_color = fcolor
            self.config = config
            self.proba = proba
            self.proba_color = proba_color


if __name__ == "__main__":
    app = AppFourmis()
    app.start()
