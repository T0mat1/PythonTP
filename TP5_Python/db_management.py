# -*- coding: utf-8 -*-
import sqlite3
from collections import defaultdict
from lxml import etree


def create_database(dbPath):
    connexion = sqlite3.connect(dbPath)
    try:
        c = connexion.cursor()

        # Create table
        # Communes
        c.execute('''CREATE TABLE IF NOT EXISTS Communes 
                        (codeDepartement, codeCommune, nomCommune, populationTotale)''')
        # Departement
        c.execute('''CREATE TABLE IF NOT EXISTS Departements
                        (codeDepartement, nomDepartement, codeRegion)''')
        # Régions
        c.execute('''CREATE TABLE IF NOT EXISTS Regions
                        (codeRegion, nomRegion)''')

        connexion.commit()
        connexion.close()
    except Exception as e:
        connexion.rollback()
        raise e


def create_table(dbPath, tableName, columns):
    connexion = sqlite3.connect(dbPath)
    try:
        c = connexion.cursor()

        # Create table
        request = "CREATE TABLE IF NOT EXISTS" + tableName + " ("
        for column in columns[:-1]:
            request += (column + ", ")
        request += (columns[-1] + ")")
        c.execute(request)

        print(request)
        connexion.commit()
        connexion.close()
    except Exception as e:
        connexion.rollback()
        raise e


def populate_table(dbPath, tableName, columns):
    connexion = sqlite3.connect(dbPath)
    try:
        c = connexion.cursor()

        request = "INSERT INTO " + tableName + " VALUES ("
        for column in columns[:-1]:
            request += ("\"" + column + "\", ")
        request += ("\"" + columns[-1] + "\")")
        # print(request)
        c.execute(request)

        connexion.commit()
        connexion.close()
    except Exception as e:
        connexion.rollback()
        raise e


def delete_data(dbPath, tableName, whereClause, whereValue):
    connexion = sqlite3.connect(dbPath)
    try:
        c = connexion.cursor()
        request = "DELETE FROM " + tableName + " WHERE " + whereClause + " LIKE \"" + whereValue + "\""
        c.execute(request)

        connexion.commit()
        connexion.close()
    except Exception as e:
        connexion.rollback()
        raise e


def insert_commune(dbPath, codeDepartement, codeComune, nomCommune, populationTotale):
    populate_table(dbPath, "Communes", [codeDepartement, codeComune, nomCommune, populationTotale])


def insert_departement(dbPath, codeDepartement, nomDepartement, codeRegion):
    populate_table(dbPath, "Departements", [codeDepartement, nomDepartement, codeRegion])


def insert_region(dbPath, codeRegion, nomRegion):
    populate_table(dbPath, "Regions", [codeRegion, nomRegion])


def delete_commune(dbPath, codeCommuneParam):
    delete_data(dbPath, "Communes", "codeCommune", codeCommuneParam)


def delete_departement(dbPath, codeDepartementParam):
    delete_data(dbPath, "Departements", "codeDepartement", codeDepartementParam)


def delete_region(dbPath, codeRegionParam):
    delete_data(dbPath, "Regions", "codeRegion", codeRegionParam)


def calculer_population_departement(dbPath, codeDepartement):
    connexion = sqlite3.connect(dbPath)
    try:
        population = 0
        c = connexion.cursor()
        request = "SELECT populationTotale FROM Communes WHERE codeDepartement =  ?"
        c.execute(request, (codeDepartement,))

        result = c.fetchall()
        for line in result:
            populationVille = line[0].replace(" ", "")
            population += int(populationVille)

        return population
    except Exception as e:
        connexion.rollback()
        raise e


def calculer_population_region(dbPath, codeRegion):
    connexion = sqlite3.connect(dbPath)
    try:
        population = 0
        c = connexion.cursor()
        request = "SELECT codeDepartement FROM Departements WHERE codeRegion =  ?"
        c.execute(request, (codeRegion,))

        result = c.fetchall()
        for line in result:
            population += calculer_population_departement(dbPath, line[0])

        return population
    except Exception as e:
        connexion.rollback()
        raise e


def search_commune_with_same_name(dbPath):
    connexion = sqlite3.connect(dbPath)
    try:
        c = connexion.cursor()
        request = '''SELECT nomCommune, codeDepartement 
                     FROM Communes 
                     WHERE nomCommune IN (
                        SELECT nomCommune 
                        FROM Communes 
                        GROUP By nomCommune 
                        HAVING COUNT(nomCommune) > 1)
                     ORDER BY nomCommune'''
        c.execute(request)

        result = c.fetchall()
        d = defaultdict(list)
        for key, value in result:
            d[key].append(value)

        for commune in list(d.items()):
            print("Nom commune :", commune[0], "; Départements :", commune[1])
    except Exception as e:
        connexion.rollback()
        raise e


def get_all_regions(dbPath):
    connexion = sqlite3.connect(dbPath)
    try:
        c = connexion.cursor()
        request = "Select * from Regions"
        c.execute(request)
        result = c.fetchall()

        connexion.commit()
        connexion.close()
        return result
    except Exception as e:
        connexion.rollback()
        raise e


def get_all_departement(dbPath):
    connexion = sqlite3.connect(dbPath)
    try:
        c = connexion.cursor()
        request = "Select * from Departements"
        c.execute(request)
        result = c.fetchall()

        connexion.commit()
        connexion.close()
        return result
    except Exception as e:
        connexion.rollback()
        raise e


def get_all_communes(dbPath):
    connexion = sqlite3.connect(dbPath)
    try:
        c = connexion.cursor()
        request = "Select * from Communes"
        c.execute(request)
        result = c.fetchall()

        connexion.commit()
        connexion.close()
        return result
    except Exception as e:
        connexion.rollback()
        raise e


def create_xml_file(dbPath, xmlFile):
    root = etree.Element("Database")
    regions = etree.SubElement(root, "Regions")
    for region in get_all_regions(dbPath):
        etree.SubElement(regions, 'Region',
                         codeRegion=region[0],
                         nomRegion=region[1])
    departements = etree.SubElement(root, "Departements")
    for departement in get_all_departement(dbPath):
        etree.SubElement(departements, 'Departement',
                         codeDepartement=departement[0],
                         nomDepartement=departement[1],
                         codeRegion=departement[2])
    communes = etree.SubElement(root, "Communes")
    for commune in get_all_communes(dbPath):
        etree.SubElement(communes, 'Commune',
                         codeDepartement=commune[0],
                         codeCommune=commune[1],
                         nomCommune=commune[2],
                         populationTotale=commune[3])
    doc = etree.ElementTree(root)
    doc.write(xmlFile, encoding='utf-8', xml_declaration=True, pretty_print=True)


def populate_db_with_xml(dbPath, xmlFile):
    create_database(dbPath)
    tree = etree.parse(xmlFile)
    for value in tree.xpath("/Database/Regions/Region"):
        insert_region(dbPath, value.attrib['codeRegion'], value.attrib['nomRegion'])
    for value in tree.xpath("/Database/Departements/Department"):
        insert_departement(dbPath, value.attrib['codeDepartement'], value.attrib['nomDepartement'],
                           value.attrib['codeRegion'])
    for value in tree.xpath("/Database/Communes/Commune"):
        insert_commune(dbPath, value.attrib['codeDepartement'], value.attrib['codeCommune'],
                       value.attrib['nomCommune'], value.attrib['populationTotale'])
if __name__ == "__main__":
    # create_table('TP5_DB_tayst.db', "taystCommmune", ["codeRegion", "codeDepartement", "nomVille", "nomAzerty", "population"])
    # populate_table('TP5_DB_tayst.db', "taystCommmune", ["14", "86", "'Poitiers'", "'PoitPoit'", "8000000000"])
    # calculer_population_departement("TP5_DB.SQLite", "86")
    # create_xml_file("TP5_DB.SQLite", "testXml.xml")
    populate_db_with_xml("TP5_XML.SQLite", "testXml.xml")
