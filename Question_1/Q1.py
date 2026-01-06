#On importe toutes les données dont nous aurons besoin

import csv

csv_premier=[]
with open('1e_aout_2025.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_premier.append(row)

csv_deuxieme=[]
with open('2e_aout_2025.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_deuxieme.append(row)

csv_troisieme=[]
with open('3e_aout_2025.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_troisieme.append(row)

csv_quatrieme=[]
with open('4e_aout_2025.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_quatrieme.append(row)

csv_cinquieme=[]
with open('5e_aout_2025.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_cinquieme.append(row)

csv_sixieme=[]
with open('6e_aout_2025.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_sixieme.append(row)

csv_septieme=[]
with open('7e_aout_2025.csv',newline='',encoding='latin-1') as csvfile:
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

#On extrait l'heure et les données sur la consommations electrique des jours

heure = []
conso_1 = []

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

#On créer une nouvelle liste et on ajoute les listes de consommation des jours dans cette liste pour faciliter le calcul de la moyenne

consommations = []
consommations.append(conso_1)
consommations.append(conso_2)
consommations.append(conso_3)
consommations.append(conso_4)
consommations.append(conso_5)
consommations.append(conso_6)
consommations.append(conso_7)

#--------------------------------------------

#On calcul la moyenne de consommation à chaque heure

nb_creneaux = 96
moyennes_15min = []

for i in range(nb_creneaux):
    somme = 0
    for jour in consommations:
        somme += int(jour[i])
    moyenne = somme / len(consommations)
    moyennes_15min.append(moyenne)


#----------------------------------------------

#print(moyennes_15min)
#print("Nombre de points :", len(moyennes_15min))

#----------------------------------------------

#Affichage du graphique

import matplotlib.pyplot as plt

plt.figure(figsize=(18, 6))
plt.bar(heure, moyennes_15min)
plt.xlabel("Heure")
plt.ylabel("Consommation moyenne")
plt.title("Consommation moyenne sur 7 jours")


plt.xticks(heure[::4]) # Pour ne pas afficher toutes les heures avec les minutes (sinon illisible)
plt.show()

        

























    

