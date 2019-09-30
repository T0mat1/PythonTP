# -*- coding: utf-8 -*-
# TP1 Python - Thomas ROSSI
from builtins import str

from date import Date


class Etudiant:

    def __init__(self, nom, prenom, date_naissance):
        self.nom = str(nom)
        self.prenom = str(prenom)
        self.date_naissance = Date(date_naissance)

    def adresselec(self):
        return self.prenom+"."+self.nom+"@etu.univ-tours.fr"


