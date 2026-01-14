import csv
import datetime
import matplotlib.pyplot as plt

# -------------------------------------------------------

donnees = []

with open("Annuel_2022.csv", newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        donnees.append(row)

with open("Annuel_2023.csv", newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        donnees.append(row)

del donnees[0]

# -------------------------------------------------------

dates = []
consommations = []

for row in donnees:
    if len(row) > 4 and row[2] != "Date" and row[4] != "":
        date_obj = datetime.datetime.strptime(row[2], "%Y-%m-%d") #conversion de la date str en date objet
        dates.append(date_obj)
        consommations.append(int(row[4]))

# -------------------------------------------------------

vacances = {
    "Toussaint": (datetime.datetime(2022, 10, 21), datetime.datetime(2022, 11, 6)),
    "Noël": (datetime.datetime(2022, 12, 23), datetime.datetime(2024, 1, 8)),
    "Hiver": (datetime.datetime(2023, 2, 17), datetime.datetime(2023, 3, 4)),
    "Printemps": (datetime.datetime(2023, 4, 13), datetime.datetime(2023, 4, 29)),
    "Été": (datetime.datetime(2023, 7, 6), datetime.datetime(2023, 12, 31))
} #initie dictionnaire avec clé = vacance, valeur = dates

# -------------------------------------------------------

conso_vacances = {nom: [] for nom in vacances} #création 1 dictionnaire = consommation pour une plage de vacance
conso_hors_vacances = []

for i in range(len(dates)):
    en_vacances = False
    for nom, (debut, fin) in vacances.items():
        if debut <= dates[i] <= fin:
            conso_vacances[nom].append(consommations[i])
            en_vacances = True
    if not en_vacances:
        conso_hors_vacances.append(consommations[i])

# -------------------------------------------------------

moy_hors = sum(conso_hors_vacances) / len(conso_hors_vacances) #calcul conso hors vacances
print("Consommation moyenne hors vacances :", moy_hors, "MW") 

for nom in conso_vacances:
    if len(conso_vacances[nom]) > 0: #verification si c'est dans la période
        moy = sum(conso_vacances[nom]) / len(conso_vacances[nom])
        print("Vacances", nom, ":", moy, "MW")

# -------------------------------------------------------

labels = []
valeurs = []

for nom in conso_vacances:
    if len(conso_vacances[nom]) > 0:
        labels.append(nom)
        valeurs.append(sum(conso_vacances[nom]) / len(conso_vacances[nom]))

plt.bar(labels, valeurs)
plt.axhline(moy_hors, linestyle='--', label="Hors vacances")
plt.legend()
plt.ylabel("Consommation (MW)")
plt.title("Consommation électrique pendant les vacances scolaires")
plt.grid()
plt.show()


