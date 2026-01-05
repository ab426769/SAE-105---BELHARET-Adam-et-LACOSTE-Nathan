
raw_data = []
processed_data = []

fichier = open('consommation_de_2019_a_2023.csv','r')
for texte in fichier  :
    texte = texte.strip("\n")
    texte = texte.split(';')
    raw_data.append(texte)
fichier.close()
print(raw_data)

for x in range(len(raw_data)) :
    for y in range(len(raw_data[x])):
        if raw_data[x][y] != '"Consommation brute"' :
            del(raw_data[y])
    print(x, raw_data[x])
    