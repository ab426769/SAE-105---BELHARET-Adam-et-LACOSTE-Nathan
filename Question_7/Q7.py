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
print(conso_cdm2022)

conso_181223 = []
for i in range(len(csv_181223)):
    conso_181223.append(csv_181223[i][4])
print(conso_181223)

conso_cdm2018 = []
for i in range(len(csv_cdm2018)):
    conso_cdm2018.append(csv_cdm2018[i][4])
print(conso_cdm2018)

conso_150719 = []
for i in range(len(csv_150719)):
    conso_150719.append(csv_150719[i][4])
print(conso_150719)

#---------------------------------------------------------------------------------




