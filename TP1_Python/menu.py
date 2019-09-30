# -*- coding: utf-8 -*-
# TP1 Python - Thomas ROSSI

from builtins import str, input, int, open
from os import path


file_name = None
DESCRIPTION = "description"
FUNCTION = "function"


def choose_file():
    """ Allow the user to choose a file """
    print("Choisissez un fichier: ")
    global file_name
    file_name = input()
    print(file_name)
    print()  # print an empty line as a separation


def add_text():
    """ Allow the user to add text to the chosen file """
    print("Entrez le texte à ajouter au fichier: ")
    if file_name is None:
        print("ERROR : Aucun fichier n'a été choisi.")
    else:
        text = input()
        file = open(file_name, "a")
        file.write(text)
        file.close()
    print()  # print an empty line as a separation


def print_file():
    """ Print all the file """
    if file_name is None:
        print("ERROR : Aucun fichier n'a été choisi.")
    else:
        file = open(file_name, "r")
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close()
    print()  # print an empty line as a separation


def empty_file():
    """ Empty the chosen file """
    if file_name is None:
        print("ERROR : Aucun fichier n'a été choisi.")
    else:
        print("Suppression du contenu du fichier")
        open('file.txt', 'w').close()
        print("Done.")
    print()  # print an empty line as a separation


FUNCTION_DICT = {1: {DESCRIPTION: "Choisir un nom de fichier", FUNCTION: choose_file},
                 2: {DESCRIPTION: "Ajouter un texte", FUNCTION: add_text},
                 3: {DESCRIPTION: "Afficher le fichier complet", FUNCTION: print_file},
                 4: {DESCRIPTION: "Vider le fichier", FUNCTION: empty_file},
                 9: {DESCRIPTION: "Quitter le programme", FUNCTION: lambda: None}}


def print_menu():
    print("====================== Menu ======================")
    if file_name is None:
        print("Aucun fichier n'a été choisi")
    else:
        print("Fichier choisi : " + path.abspath(file_name))
    for e in FUNCTION_DICT:
        print(str(e)+". "+FUNCTION_DICT[e][DESCRIPTION])


if __name__ == "__main__":
    choice = 0
    while choice is not 9:
        print_menu()
        user_input = input()
        choice = int(user_input)
        FUNCTION_DICT[choice][FUNCTION]()
