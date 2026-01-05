import csv

excel_global=[]
with open('conso_3.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        excel_global.append(row)
#print(excel_global)


#---------------------------------------------------------------------------------------------------

#Question 4 - Différence entre Ete et Hiver
import csv

excel_hiver=[]
with open('conso_hiver.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        excel_hiver.append(row)

debut_hiver = '2024/12/21'
annee, mois, jour = debut_hiver.split("/")
conversion_debut_hiver = int(annee) * 365 + int(mois) * 30 + int(jour)

fin_hiver = '2025/03/20'
annee, mois, jour = fin_hiver.split("/")
conversion_fin_hiver = int(annee) * 365 + int(mois) * 30 + int(jour)

temps = [] #Création d'une liste avec uniquement les dates
for i in range(len(excel_hiver)):
    temps.append(excel_hiver[i][0])
del temps[0]

jours = []
for d in temps: #Conversion des dates en jour
    annee, mois, jour = d.split("/")
    total = int(annee) * 365 + int(mois) * 30 + int(jour)
    jours.append(total)

for i in jours :
    if conversion_debut_hiver <= i <= conversion_fin_hiver:
        print(i)


