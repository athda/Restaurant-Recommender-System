#les fonctions utilisées
import pandas
import json
import numpy

#########################################-etape 1 du prétraitement(la lecture)-#########################################################
# la fonction qui va des imbriquer les données recuperés à partir d'un fichier json et les stocker en csv
# puisqu'on va travailler avec des fichiers json grand on a ajouté deux paramétres n_i et n_f qui indiquent
# l'intervalle de lignes qu'on va traiter
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
def delete_empty_columns(df):
    for (columnName, columnData) in df.iteritems():
        if(df[columnName].isnull().sum() * 100 / len(df) == 100):
            df=df.drop(columnName, axis=1)
    return df
#########################################-etape 2 du prétraitement(le nettoyage)-#########################################################
#
# traitement des valeurs nulls
#
# suprimer les clonnes qui ont un pourcentage de valeurs null superieur à un certain seuil
def delete_null_columns(df):
    for (columnName, columnData) in df.iteritems():
        if(df[columnName].isnull().sum() * 100 / len(df)>50):
            df=df.drop(columnName, axis=1)
    return df
#la fonction qui remplce les valeurs null par les valeurs les plus fréquentes
def remplace_null_columns(df):
    df=df.replace(to_replace='None', value=numpy.nan)
    df = df.fillna(df.mode().iloc[0])
    return df
#
# statistiques /visualisation
# il y a plusieurs fontions simples qui nous permet d'obtenir des informations sur les données
# df.info()  / df.head() "afficher les 5 premiers lignes du tableau" / df.describe() "presque similaire a df.info()"
# la fonction qui affiche le pourcentage des valeurs null de chaque colonne du tableau
def percentage_null(df):
    print(df.isnull().sum() * 100 / len(df))
# la fonction qui affiche toutes les valeurs possibles pour chaque colone du tableau
def column_values(df):
    for (column, columnData) in df.iteritems():
        print(column,"\n", df[column].value_counts(), "\n")
#remplacer une chaine de caractére par une autre dans une colonne doc : pandas.DataFrame.replace.html
def remplace_string_column(df,column,old_string,new_string):
    df.loc[df[column] == old_string, column] = new_string
#########################################-etape 3 du prétraitement(data-mining)-#########################################################
#coder une colone du tableau <<non fini
def encode_column(df,column):
    df[column]=df[column].astype('category').cat.codes

