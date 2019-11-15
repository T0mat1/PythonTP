# -*- coding: utf-8 -*-
import sqlite3


def create_database(dbPath):
    connexion = sqlite3.connect(dbPath)
    c = connexion.cursor()

    # Create table
    # Communes
    c.execute('''CREATE TABLE Communes 
                (codeRegion, nomRegion, codeDepartement,codeArrondissement, codeCanton, codeCommune, nomCommune,
                 populationMunicipale, populationCompteeAPart, populationTotale)''')
    # Departement
    c.execute('''CREATE TABLE Departements
                (codeRegion, nomRegion, codeDepartement, nomDepartement, nombreArrondissements, nombreCantons,
                 nombresCommunes, populationMunicipale, populationTotale )''')
    # Régions
    c.execute('''CREATE TABLE Regions
                (codeRegion, nomRegion, nombreArrondissements, nombreCantons, nombreCommunes,
                 populationMunicipale, populationTotale)''')

    connexion.commit()
    connexion.close()


def create_table(dbPath, tableName, columns):
    connexion = sqlite3.connect(dbPath)
    c = connexion.cursor()

    # Create table
    request = "CREATE TABLE " + tableName + " ("
    for column in columns[:-1]:
        request += (column + ", ")
    request += (columns[-1] + ")")
    c.execute(request)

    print(request)
    connexion.commit()
    connexion.close()

def populate_table(dbPath, tableName, columns):
    connexion = sqlite3.connect(dbPath)
    c = connexion.cursor()

    request = "INSERT INTO " + tableName + " VALUES ("
    for column in columns[:-1]:
        request += (column + ", ")
    request += (columns[-1] + ")")
    c.execute(request)

    print(request)
    connexion.commit()
    connexion.close()

# if __name__ == "__main__":
#     create_table('TP5_DB_tayst.db', "taystCommmune", ["codeRegion", "codeDepartement", "nomVille", "nomAzerty", "population"])
    # populate_table('TP5_DB_tayst.db', "taystCommmune", ["14", "86", "'Poitiers'", "'PoitPoit'", "8000000000"])