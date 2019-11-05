# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random as r
# init values
n = 100
(a, b) = (0, 100)

# 1. Générer des nombres aléatoires
random_list = [r.randint(a, b) for _ in range(n)]

# 2. Afficher la courbe de ces données dans une fenêtre matplotlib
# plt.plot(random_list)
# plt.show()

# 3. Afficher plusieurs courbes avec styles et couleurs variés
plt.plot(list(map(lambda x: x, list(range(0,100)))), "r--")
plt.plot(list(map(lambda x: x*x, list(range(0,100)))), "b.")
plt.plot(list(map(lambda x: 2*x+8, list(range(0,100)))), "y")
plt.axis([0, 10, 0, 100])
plt.show()

# 4. Modifier les noms des axes, la légende, ajouter des flèches pour montrer des zones…

# 5. Afficher un histogramme et un camembert

# 6. Afficher une surface 2D dans un espace 3D (mesh)

