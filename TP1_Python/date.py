# -*- coding: utf-8 -*-
# TP1 Python - Thomas ROSSI

from builtins import type, int


class Date:

    def __init__(self, jour, mois, annee):
        self.jour = int(jour)
        self.mois = int(mois)
        self.annee = int(annee)

    def __init__(self, date):
        data = date.split("/")
        self.jour = int(data[0])
        self.mois = int(data[1])
        self.annee = int(data[2])

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.jour == other.jour and self.mois == other.jour and self.annee == other.annee

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        res = self.annee < other.annee
        if self.annee == other.annee:
            res = self.mois < other.mois
            if self.mois == other.mois:
                res = self.jour < other.jour
        return res

    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)