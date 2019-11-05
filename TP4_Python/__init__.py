# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random as r
n = 100
(a, b) = (0, 100)
random_list = [r.randint(a, b) for _ in range(n)]

plt.plot(random_list)
plt.ylabel('Label 1')
plt.show()

