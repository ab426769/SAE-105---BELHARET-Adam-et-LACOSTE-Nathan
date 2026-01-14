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
        try:
            cleaned_data.append(float(Mr_ours[0]))
        except:
            cleaned_data.append(np.nan)
    return cleaned_data

def processing(processed_data,data_type) :
    octaling = []
    inkling = []
    
    if data_type == 'conso' :  
        for agent_4 in range(len(low_processed_data)) :
            if low_processed_data[agent_4][1] == '' :
                inkling.append(no_data)
            else :
                inkling.append(low_processed_data[agent_4][1].split(','))
                del inkling[agent_4][1]
        return inkling   
        
    elif data_type == 'dates':
        for agent_4 in range(len(low_processed_data)) :
            octaling.append(low_processed_data[agent_4][0])  
        return octaling
    
raw_data = []                     # données brutes
low_processed_data = []           # dates + conso
processed_data_1 = []             # conso
processed_data_2 = []             # dates
no_data = [np.nan]                # donnée non existante

#-----------------------------------------------------------------------------------
# ouverture du fichier et extraction des données brute

fichier = open('consommation_de_2019_a_2023.csv', 'r')

for texte in fichier:
    texte = texte.strip("\n")
    texte = texte.split(';')
    raw_data.append(texte)

fichier.close()
    
#print(raw_data)
    
#-----------------------------------------------------------------------------------
# traitment des données afin de n'avoir que celle de 2020
    
for ayo in range(len(raw_data)):
    del raw_data[ayo][1]
    del raw_data[ayo][2]
    if ayo < 733 :
        low_processed_data.append(raw_data[ayo])
del low_processed_data[0]
    
#print(low_processed_data)

#-----------------------------------------------------------------------------------
# traitment des données afin de séparer les dates et les consommations 
    
processed_data_1 = processing(low_processed_data,'conso')
processed_data_2 = processing(low_processed_data,'dates')
    
#print(processed_data_1)
#print(processed_data_2)
    
    
#-----------------------------------------------------------------------------------
# formatage des dates et nettoyage des données

x = [datetime.strptime(d, "%Y/%m/%d") for d in processed_data_2]
y = cleaning(processed_data_1)

#-----------------------------------------------------------------------------------
# création du graphique 

plt.figure(figsize=(14,8))
plt.plot(x, y, label="Consommation 2020", color='magenta')

plt.xlabel("Date")
plt.ylabel("Consommation en GW")
plt.title("Consommation d'électricité en 2020")
plt.legend()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
