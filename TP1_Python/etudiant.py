# -*- coding: utf-8 -*-
# TP1 Python - Thomas ROSSI
import unidecode
from builtins import str
from TP1_Python.date import Date
from datetime import date as d


class Etudiant:

    def __init__(self, nom, prenom, date_naissance):
        self.nom = str(nom)
        self.prenom = str(prenom)
        self.date_naissance = Date(date_naissance)

    def adresselec(self):
        nom = unidecode.unidecode(self.nom).replace(" ", "").lower()
        prenom = unidecode.unidecode(self.prenom).replace(" ", "").lower()
        return prenom+"."+nom+"@etu.univ-tours.fr"

    def age(self):
        today = d.today()
        age = today.year - self.date_naissance.annee
        if today.month < self.date_naissance.mois or (today.month == self.date_naissance.mois and today.day < self.date_naissance.jour):
            age -= 1
        return age

    def __str__(self):
        return self.prenom+" "+self.nom

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    students = []
    for line in open(".\\fichetu.csv","r").readlines():
        data = line.split(";")
        students.append(Etudiant(data[0], data[1], data[2]))
    print(str(students))
