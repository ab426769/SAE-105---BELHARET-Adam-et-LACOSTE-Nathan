#-----------------------------------------------------------------------------------
# importation des modules 

import csv
import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

#-----------------------------------------------------------------------------------
# definition des fonctions et listes 

def cleaning(data):
    cleaned_data = []
    for Mr_ours in data:
        if Mr_ours == [np.nan] or Mr_ours == []:
            cleaned_data.append(np.nan)
        else:
            cleaned_data.append(float(Mr_ours[0]))
    return cleaned_data

def heavy_processing(processed_data,data_type) :
    octaling = []
    inkling = []
    
    if data_type == 'conso' :    
        for agent_4 in range(len(processed_data)) :
            if processed_data[agent_4][1] == '' :
                inkling.append(no_data)
            else :
                inkling.append(processed_data[agent_4][1].split(','))
                del inkling[agent_4][1]      
        return inkling   
    
    elif data_type == 'dates':
        for agent_4 in range(len(processed_data)) :
            octaling.append(processed_data[agent_4][0])  
        return octaling

raw_data = []                     # données brutes
low_processed_data = []           # données de 2021/2022/2023
processed_data_1 = []             # données de 2021 (date + conso)
processed_data_2 = []             # données de 2022 (date + conso)
processed_data_3 = []             # données de 2023 (date + conso)
heavy_processed_data_1 = []       # données de 2021 (consommation)
heavy_processed_data_2 = []       # données de 2022 (consommation)
heavy_processed_data_3 = []       # données de 2023 (consommation)
heavy_processed_data_4 = []       # données de 2021 (dates)
heavy_processed_data_5 = []       # données de 2022 (dates)
heavy_processed_data_6 = []       # données de 2023 (dates)
no_data = [np.nan]                # donnée non existante

#-----------------------------------------------------------------------------------
# ouverture du fichier et extraction des données brutes

fichier = open('consommation_de_2019_a_2023.csv', 'r')

for texte in fichier:
    texte = texte.strip("\n")
    texte = texte.split(';')
    raw_data.append(texte)

fichier.close()

#print(raw_data)

#-----------------------------------------------------------------------------------
# traitment des données afin de les regrouper par années

for ayo in range(len(raw_data)):
    del raw_data[ayo][1]
    del raw_data[ayo][2]
    if ayo > 733 and ayo < 2923 :
        low_processed_data.append(raw_data[ayo])

#print(low_processed_data)

for oly in range(len(low_processed_data)) :
    if oly < 729 :
        processed_data_1.append(low_processed_data[oly])
    elif oly > 728 and oly < 1459 :
        processed_data_2.append(low_processed_data[oly])
    else :
        processed_data_3.append(low_processed_data[oly])

#print(processed_data_1)
#print(processed_data_2)
#print(processed_data_3)

#-----------------------------------------------------------------------------------
# traitment des données afin de séparer les dates et les consommations 

heavy_processed_data_1 = heavy_processing(processed_data_1,'conso')
heavy_processed_data_2 = heavy_processing(processed_data_2,'conso')
heavy_processed_data_3 = heavy_processing(processed_data_3,'conso')
heavy_processed_data_4 = heavy_processing(processed_data_1,'dates')
heavy_processed_data_5 = heavy_processing(processed_data_2,'dates')
heavy_processed_data_6 = heavy_processing(processed_data_3,'dates')

#-----------------------------------------------------------------------------------
# nettoyage des données et formatage des dates 

y1 = cleaning(heavy_processed_data_1)
y2 = cleaning(heavy_processed_data_2)
y3 = cleaning(heavy_processed_data_3)

x1 = [datetime.strptime(d, "%Y/%m/%d") for d in heavy_processed_data_4]
x2 = [datetime.strptime(d, "%Y/%m/%d") for d in heavy_processed_data_5]
x3 = [datetime.strptime(d, "%Y/%m/%d") for d in heavy_processed_data_6]

#-----------------------------------------------------------------------------------
# création du graphique

plt.figure(figsize=(14,8))

plt.plot(x1, y1, label="Consommation 2021", color='green')
plt.plot(x2, y2, label="Consommation 2022", color='red')
plt.plot(x3, y3, label="Consommation 2023", color='blue')

plt.xlabel("Date")
plt.ylabel("Consommation en GW")
plt.title("Consommation d'électricité en fonction du temps")
plt.legend()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()

