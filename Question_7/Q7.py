import csv

csv_cdm2022=[]
with open('CDM_2022.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_cdm2022.append(row)

csv_181223=[]
with open('18_decembre_2023.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_181223.append(row)

csv_cdm2018=[]
with open('CDM_2018.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_cdm2018.append(row)

csv_150719=[]
with open('15_juillet_2019.csv',newline='',encoding='latin-1') as csvfile:
    reader=csv.reader(csvfile,delimiter='\t')
    for row in reader:
        csv_150719.append(row)

#---------------------------------------------------------------------------------

del csv_cdm2022[97]
del csv_cdm2022[0]
del csv_cdm2018[97]
del csv_cdm2018[0]
del csv_181223[97]
del csv_181223[0]
del csv_150719[97]
del csv_150719[0]

#---------------------------------------------------------------------------------

heure = []

conso_cdm2022 = []
for i in range(len(csv_cdm2022)):
    heure.append(csv_cdm2022[i][3])
    conso_cdm2022.append(csv_cdm2022[i][4])

conso_181223 = []
for i in range(len(csv_181223)):
    conso_181223.append(csv_181223[i][4])

conso_cdm2018 = []
for i in range(len(csv_cdm2018)):
    conso_cdm2018.append(csv_cdm2018[i][4])

conso_150719 = []
for i in range(len(csv_150719)):
    conso_150719.append(csv_150719[i][4])


#----------------------------------------------------------------------------------

conso_cdm2022[:] = [x for x in conso_cdm2022 if x != ""]
conso_cdm2022 = [int(x) for x in conso_cdm2022]
#print(conso_cdm2022)

conso_cdm2018[:] = [x for x in conso_cdm2018 if x != ""]
conso_cdm2018 = [int(x) for x in conso_cdm2018]
#print(conso_cdm2018)

conso_181223[:] = [x for x in conso_181223 if x != ""]
conso_181223 = [int(x) for x in conso_181223]
#print(conso_181223)

conso_150719[:] = [x for x in conso_150719 if x != ""]
conso_150719 = [int(x) for x in conso_150719]
#print(conso_150719)

heure[:] = heure[::2] #change la base de temps de pas 15 à pas 30 minutes

#print(len(conso_cdm2022))
#print(len(conso_181223))
#print(len(heure))
#print(heure)

   

#-----------------------------------------------------------------------------------

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Premier graphique : CDM 2018 vs Un an après
axes[0].plot(heure, conso_cdm2018, label="CDM 2018", color="blue", marker='o')
axes[0].plot(heure, conso_150719, label="15/07/2019", color="green", marker='o')
axes[0].set_title("Comparaison CDM 2018 vs Un an après")
axes[0].set_ylabel("Consommation")
axes[0].legend()
axes[0].grid(True)
axes[0].set_xticks(heure[::2])
axes[0].set_xticklabels(heure[::2], rotation=45)

# Deuxième graphique : CDM 2022 vs Un an après
axes[1].plot(heure, conso_cdm2022, label="CDM 2022", color="red", marker='o')
axes[1].plot(heure, conso_181223, label="18/12/23", color="orange", marker='o')
axes[1].set_title("Comparaison CDM 2022 vs Un an après")
axes[1].set_xlabel("Heure")
axes[1].set_ylabel("Consommation")
axes[1].legend()
axes[1].grid(True)
axes[1].set_xticks(heure[::2])
axes[1].set_xticklabels(heure[::2], rotation=45)

plt.tight_layout()
plt.show()


