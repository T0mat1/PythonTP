# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
import random as r

# init values
n = 200
(a, b) = (0, 200)

# 1. Générer des nombres aléatoires
random_list = [r.randint(a, b) for _ in range(n)]

# 2. Afficher la courbe de ces données dans une fenêtre matplotlib
plt.plot(random_list)
plt.show()

# 3. Afficher plusieurs courbes avec styles et couleurs variés
plt.plot(list(map(lambda x: x, list(range(0,100)))), "r--")
plt.plot(list(map(lambda x: x*x, list(range(0,100)))), "b.")
plt.plot(list(map(lambda x: 2*x+8, list(range(0,100)))), "y")
plt.axis([0, 10, 0, 100])
plt.show()

# 4. Modifier les noms des axes, la légende, ajouter des flèches pour montrer des zones…
# Noms des axes
plt.plot(random_list, label="Random data")
plt.plot(list(map(lambda x: math.log(x)**3, list(range(1, 200)))), 'r', label="log(x)³")
plt.xlabel('Axe des x')
plt.ylabel('Axe des y')

# Mettre une légende
plt.legend()  # à l'aide des labels des plots

# Ajouter des flèches
plt.grid(True)
min_point = (random_list.index(min(random_list)), min(random_list))
max_point = (random_list.index(max(random_list)), max(random_list))
plt.annotate('Minimum', xy=min_point, xytext=(min_point[0]+20, min_point[1]-10),
             arrowprops={'facecolor': 'black', 'shrink': 0.05})
plt.annotate('Maximum', xy=max_point, xytext=(max_point[0]-20, max_point[1]+20),
             arrowprops={'facecolor': 'black', 'shrink': 0.05})
plt.show()

# 5. Afficher un histogramme et un camembert

# histogramme
# 200 tirages entre 0 et 6
effectifs = [r.randint(1, 6) for i in range(200)]
n, bins, patches = plt.hist(effectifs, 15, density=1, facecolor='b', alpha=0.5)

plt.xlabel('Numéro')
plt.ylabel(u'Probabilité')
plt.grid(True)
plt.show()

# camembert
name = ['Data1', 'Data2', 'Data3', 'Data4', 'Data5']
data = [r.randint(a, b) for _ in range(5)]

explode = (0, 0.15, 0, 0)
plt.pie(data, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis('equal')
plt.show()

# 6. Afficher une surface 2D dans un espace 3D (mesh)
