import csv

csv_premier=[]
with open('1e_decembre.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_premier.append(row)

csv_deuxieme=[]
with open('2e_decembre.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_deuxieme.append(row)

csv_troisieme=[]
with open('3e_decembre.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_troisieme.append(row)

csv_quatrieme=[]
with open('4e_decembre.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_quatrieme.append(row)

csv_cinquieme=[]
with open('5e_decembre.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_cinquieme.append(row)

csv_sixieme=[]
with open('6e_decembre.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_sixieme.append(row)

csv_septieme=[]
with open('7e_decembre.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_septieme.append(row)

#-----------------------------------------------------------------------

#On supprime la première et dernière ligne du fichier afin de ne pas avoir du soucis lors du traitement de ces derniers

del csv_premier[97]
del csv_premier[0]
del csv_deuxieme[97]
del csv_deuxieme[0]
del csv_troisieme[97]
del csv_troisieme[0]
del csv_quatrieme[97]
del csv_quatrieme[0]
del csv_cinquieme[97]
del csv_cinquieme[0]
del csv_sixieme[97]
del csv_sixieme[0]
del csv_septieme[97]
del csv_septieme[0]

#-----------------------------------------------------

conso_1 = []
heure = []

for i in range(len(csv_premier)):
    heure.append(csv_premier[i][3])
    conso_1.append(csv_premier[i][4])

conso_2 = []
for i in range(len(csv_deuxieme)):
    conso_2.append(csv_deuxieme[i][4])

conso_3 = []
for i in range(len(csv_troisieme)):
    conso_3.append(csv_troisieme[i][4])

conso_4 = []
for i in range(len(csv_quatrieme)):
    conso_4.append(csv_quatrieme[i][4])

conso_5 = []
for i in range(len(csv_cinquieme)):
    conso_5.append(csv_cinquieme[i][4])

conso_6 = []
for i in range(len(csv_sixieme)):
    conso_6.append(csv_sixieme[i][4])

conso_7 = []
for i in range(len(csv_septieme)):
    conso_7.append(csv_septieme[i][4])


#--------------------------------------------

consommations_ouvres = []
consommations_wk = []
consommations_ouvres.append(conso_1)
consommations_ouvres.append(conso_2)
consommations_ouvres.append(conso_3)
consommations_ouvres.append(conso_4)
consommations_ouvres.append(conso_5)
consommations_wk.append(conso_6)
consommations_wk.append(conso_7)

#print(consommations_ouvres)
#print(consommations_wk)

#--------------------------------------------

nb_creneaux = 96
moyenne_ouvres = []
moyenne_wk = []

for i in range(nb_creneaux):
    somme = 0
    for jour in consommations_ouvres:
        somme += int(jour[i])
    moyenne = somme / len(consommations_ouvres)
    moyenne_ouvres.append(moyenne)

for i in range(nb_creneaux):
    somme = 0
    for jour in consommations_wk:
        somme += int(jour[i])
    moyenne = somme / len(consommations_wk)
    moyenne_wk.append(moyenne)

print(moyenne_ouvres)
print(moyenne_wk)

#-------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np


# Création du graphique
plt.figure(figsize=(15,6))
plt.plot(heure, moyenne_ouvres, label="Jours ouvrés", color='blue')
plt.plot(heure, moyenne_wk, label="Week-end", color='orange')
plt.xlabel("Heure de la journée")
plt.ylabel("Consommation électrique")
plt.title("Comparaison consommation électrique : jours ouvrés vs week-end")
plt.xticks(heure[::4])
plt.legend()
plt.grid(True)
plt.show()

