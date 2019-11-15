# -*- coding: utf-8 -*-
# TP5 - Thomas ROSSI & Emeric PAIN


def read_csv_file(filename, enc="utf-8"):
    with open(filename, 'r', encoding=enc) as file:
        data = []
        lines = file.readlines()
        columns =lines[7].split(";")
        for line in lines[8:-1]:
            data.append(line.split(";")[:-1])
        return columns, data


if __name__ == "__main__":
    # main execution for test purpose
    col, dat = read_csv_file("C:\\Users\\Tomati\\Downloads\\communes.csv", "cp1252")
    print("Colonnes:")
    print(col)
    print("Données:")
    for d in dat[:20]:
        print(d)