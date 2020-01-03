# -*- coding: utf-8 -*-
# TP1 Python - Thomas ROSSI & Emeric PAIN

from builtins import type, int


def is_a_leap_year(year):
    if year % 4 == 0:
        if (year % 100 == 0 and year % 400 == 0) or year % 100 != 0:
            return True
    return False


def get_number_of_days_in_month(month, year):
    month = int(month); year = int(year)  # Make sure that year and month are integers
    assert month in range(1, 13), "Le mois (%d) n'est pas compris dans l'intervalle [1,12]" % month
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if is_a_leap_year(year):
            return 29
        else:
            return 28
    else:
        raise ValueError


class Date:

    def __init__(self, jour, mois, annee):
        assert jour <= get_number_of_days_in_month(mois, annee), "Le jour indiqué (%d) n'existe pas pour le mois et l'année donnés" % jour
        self.jour = int(jour)
        self.mois = int(mois)
        self.annee = int(annee)

    def __init__(self, date):
        data = date.split("/")
        assert int(data[0]) <= get_number_of_days_in_month(data[1], data[2]), "Le jour indiqué (%s) n'existe pas pour le mois et l'année donnés" % data[0]
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

    def __str__(self):
        return "%02d/%02d/%d" % (self.jour, self.mois, self.annee)
