import sqlite3
import os
print('========================')
print('Bonjour ')
print('========================')
Nom_DB = str(input('Donner Une Nom Pour La Base De Donner  '))
connection = sqlite3.connect(f"{Nom_DB}.db")
cursor = connection.cursor()
directory = os.getcwd()
Nb_Table = int(input(f"Combien De Tables Voulez Vouz Ajouter a La Base De Donnée {Nom_DB} ?  "))
i = 1
while (i <= Nb_Table):
    Nom_Table = str(input(f"Donner Le Nom De La Table {i} Correspend A La Base de Donnée {Nom_DB}  "))
    Nb_Col = int(input(f"Combien De column Voulez Vous Ajouter Dans La Table {Nom_Table}  "))
    j = 1
    for j in range(1):
        Nom_Col = str(input(f"Donner Le Nom De La Column {j+1} CCorrespend a La Table {Nom_Table}   "))
        print('========================')
        print(f"Donner Le Type De La Column {Nom_Col}")
        print('========================')
        print('Pour Choisir "Entier" Tapez 1')
        print('Pour Choisir "Reel" Tapez 2')
        print('Pour Choisir "Text" Tapez 3')
        Type_Col = int(input(f"Tapez Votre Choix ...   "))
        if (Type_Col == 1):
            cursor.execute(f"CREATE TABLE {Nom_Table}({Nom_Col} INTEGER)  ")
            connection.commit()
        elif (Type_Col == 2):
            cursor.execute(f"CREATE TABLE {Nom_Table}({Nom_Col} FLOAT)  ")
            connection.commit()
        elif (Type_Col == 3):
            cursor.execute(f"CREATE TABLE {Nom_Table}({Nom_Col} TEXT)  ")
            connection.commit()
    j = 2
    for j in range(Nb_Col-1):
        Nom_Col = str(input(f"Donner Le Nom De La Column {j+2} Correspend a La Table {Nom_Table}   "))
        print('========================')
        print(f"Donner Le Type De La Column {Nom_Col}")
        print('========================')
        print('Pour Choisir "Entier" Tapez 1')
        print('Pour Choisir "Reel" Tapez 2')
        print('Pour Choisir "Text" Tapez 3')
        Type_Col = int(input(f"Tapez Votre Choix ...   "))
        if (Type_Col == 1):
            cursor.execute(f"ALTER TABLE {Nom_Table} ADD {Nom_Col} INTEGER")
            connection.commit()
        elif (Type_Col == 2):
            cursor.execute(f"ALTER TABLE {Nom_Table} ADD {Nom_Col} FLOAT")
            connection.commit()
        elif (Type_Col == 3):
            cursor.execute(f"ALTER TABLE {Nom_Table} ADD {Nom_Col} TEXT")
            connection.commit()
    i += 1
print('=========================================================')
print("Votre Base De Donnée A été Créé Avec Succès ")
print(f"Vous Pouvez Trouver Le Ficher {Nom_DB}.db Dans Cette Repertoire ")
print(f"{directory}\{Nom_DB}.db")
print('=========================================================')







