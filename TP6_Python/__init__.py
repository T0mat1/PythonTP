# -*- coding: utf-8 -*-
# TP6 - Emeric Pain & Thomas Rossi

import numpy as np
from random import randint
from random import seed


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


if __name__ == "__main__":
    seed(2)
    #question1()
    #question2()
    question3()
