# -*- coding: utf-8 -*-
# Authors Thomas Rossi  & Emeric Pain
import threading
from datetime import datetime
from multiprocessing import Process

n = 1E8

def reset():
    n = 1E8

def calcul_long():
    global n
    while n > 0:
        n -= 1


if __name__ == "__main__":
    starting_time = datetime.now()
    print("Single thread program started at", starting_time)
    calcul_long()
    print("Single thread program has ran for", datetime.now()-starting_time)
    reset()

    starting_time = datetime.now()
    print("Multi thread program started at", starting_time)
    for i in range(3):
        threading.Thread(target=calcul_long).start()
    print("Multi thread program has ran for", datetime.now() - starting_time)
    reset()

    starting_time = datetime.now()
    print("Multi process program started at", starting_time)
    for i in range(3):
        p = Process(target=calcul_long)
        p.start()
    print("Multi process program has ran for", datetime.now()-starting_time)

