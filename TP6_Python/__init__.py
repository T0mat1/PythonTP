# -*- coding: utf-8 -*-
# TP6 - Emeric Pain & Thomas Rossi

import numpy as np
from scipy import optimize
from scipy import interpolate
import matplotlib.pyplot as plt
from random import randint, seed, random


def question1():
    print("\n============= QUESTION 1 =============")
    lower = 0
    upper = 100
    shape = (4, 3, 2)

    random_3d_array = np.array([randint(lower, upper) for _ in range(4 * 3 * 2)]).reshape(shape)

    print("Nombre de dimensions:", random_3d_array.ndim)
    print("Forme du tableau:", random_3d_array.shape)
    print("Taille du tableau:", random_3d_array.size)
    print("Type des données:", random_3d_array.dtype)
    print("Espace mémoire du tableau (en octets):", random_3d_array.itemsize)
    print("Données: %s\n" % random_3d_array.data, random_3d_array)


def question2():
    print("\n============= QUESTION 2 =============")
    matrix_1 = np.array([[randint(0, 8) for _ in range(3)] for _ in range(3)])
    matrix_2 = np.array([[randint(2, 10) for _ in range(3)] for _ in range(3)])

    print("M1 =\n", matrix_1)
    print("M2 =\n", matrix_2)
    print("M1.M2 =\n", matrix_1.dot(matrix_2))
    print("Transposée de M1:\n", matrix_1.T)


def question3():
    print("\n============= QUESTION 3 =============")
    matrix = np.array([[randint(0, 10) for _ in range(3)] for _ in range(3)])
    vector = np.array([randint(0, 10) for _ in range(3)]).transpose()
    det_matrix = round(np.linalg.det(matrix))

    print("M =\n", matrix)
    print("det(M) = ", det_matrix) # affiche le déterminant de la matrice
    # affiche la matrice inverse si elle existe
    print("M⁻¹ =\n", np.linalg.inv(matrix)) if det_matrix != 0.0 else print("Le déterminant est 0, il n'existe pas de "
                                                                            "matrice inverse.")
    print("V = ", vector)
    # résoud le système linéaire MX = V
    print("MX = V <=> X =\n", np.linalg.solve(matrix, vector))
    print("Valeurs propres :", np.linalg.eigvals(matrix))
    print("Vecteurs propres :")
    for vecteur_propre in np.linalg.eigh(matrix)[1]:
        print(vecteur_propre)


def question4():
    print("\n============= QUESTION 4 =============")
    fonction_carre = lambda x: x*x
    fonction_affine = lambda x: 20*x+3
    liste_points_carre = [fonction_carre(x)+(random()-0.5)*5 for x in range(0, 20)]
    liste_points_affine = [fonction_affine(x)+(random()-0.5)*5 for x in range(0, 20)]
    plt.plot(liste_points_carre, 'b.', label="x²")
    plt.plot(liste_points_affine, 'r.', label="20x+3")
    plt.legend()
    plt.show()
    curve_carre = list(optimize.curve_fit(f=fonction_carre, xdata=range(0, 20), ydata=liste_points_carre))
    curve_affine = list(optimize.curve_fit(f=fonction_affine, xdata=range(0, 20), ydata=liste_points_affine))
    plt.plot(curve_carre, 'b', label="x²")
    plt.plot(curve_affine, 'r', label="20x+3")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    seed(2)
    #question1()
    #question2()
    #question3()
    question4()

