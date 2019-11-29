# -*- coding: utf-8 -*-
import TP5_Python.db_management as db_management
import TP5_Python.parser_csv as parser_csv
from termcolor import colored

def calculer_population_departement_et_comparer(dataDepartement, dbPath):
    for departement in dataDepartement:
        print("-----------------")
        print("Departement :", departement[3])
        populationCalcule = db_management.calculer_population_departement(dbPath, departement[2])
        print("Population calculée :", populationCalcule)
        populationAttendue = int(departement[8].replace(" ", ""))
        print("Population attendue : ", populationAttendue)
        if(populationCalcule == populationAttendue):
            print(colored("Les 2 valeurs sont égales", "green"))
        else:
            print(colored("Les 2 valeurs sont différentes", "red"))
        print()


def calculer_population_region_et_comparer(dataRegion, dbPath):
    for region in dataRegion:
        print("-----------------")
        print("Région :", region[1])
        populationCalcule = db_management.calculer_population_region(dbPath, region[0])
        print("Population calculée :", populationCalcule)
        populationAttendue = int(region[6].replace(" ", ""))
        print("Population attendue : ", populationAttendue)
        if(populationCalcule == populationAttendue):
            print(colored("Les 2 valeurs sont égales", "green"))
        else:
            print(colored("Les 2 valeurs sont différentes", "red"))
        print()

if __name__ == "__main__":
    dbPath = "TP5_DB.SQLite"
    db_management.create_database(dbPath)
    _, dataRegions = parser_csv.read_csv_file("regions.csv", "cp1252")
    # for region in dataRegions:
    #     db_management.insert_region(dbPath, region[0], region[1])
    _, dataDepartement = parser_csv.read_csv_file("departements.csv", "cp1252")
    # for departement in dataDepartement:
    #     db_management.insert_departement(dbPath, departement[2], departement[3], departement[0])
    _, dataCommunes = parser_csv.read_csv_file("communes.csv", "cp1252")
    # for commune in dataCommunes:
    #     db_management.insert_commune(dbPath, commune[2], commune[5], commune[6], commune[9])
    # calculer_population_departement_et_comparer(dataDepartement, dbPath)
    # calculer_population_region_et_comparer(dataRegions, dbPath)
    db_management.search_commune_with_same_name(dbPath)

