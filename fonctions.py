#les fonctions utilisées
import pandas
import json


# la fonction qui va des imbriquer les données recuperés à partir d'un fichier json et les stocker en csv
# puisqu'on va travailler avec des fichiers json grand on a ajouté deux paramétres n_i et n_f qui indiquent l'intervalle de lignes qu'on va traiter
def des_imbriquer(input_json, output_csv, n_i=0, n_f=1000050):
    json_data = []  # le tableu
    json_file = input_json
    file = open(json_file)
    i = 0
    for line in file:
        if i < n_i:
            i = i + 1
        elif i >= n_i and i < n_f:
            json_line = json.loads(line)
            json_data.append(json_line)
            i = i + 1
        else:
            break
    df = pandas.json_normalize(json_data)

    df.to_csv(output_csv, index=False)
    df.head()
# fonction qui compte le nombre des lignes dans un fichier elle nous
# retourn le nombre d'objets dans un fichier json
def count_file_lines(input_file):
    file = open(input_file)
    i = 0
    for line in file:
        i = i + 1
    return i
