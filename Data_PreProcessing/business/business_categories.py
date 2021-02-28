import pandas as pd
from fonctions import *
import matplotlib.pyplot as plt
import numpy as np
import re
import math
import seaborn as sns


def remove_space(word):
    return re.sub(r"^\s+|\s+$", '', word)


def get_all_different_categories(df):

    df_business = df[df['categories'].notna()]
    categories = ';'.join(df_business['categories'])
    all_categories = re.split(';|,', categories)

    #Create a new df with all extracted categories
    data = {'Categorie':  all_categories}
    df_categories = pd.DataFrame (data, columns = ['Categorie'])

    #remove spaces => to compare categories
    df_categories['Categorie'] =df_categories['Categorie'].apply(remove_space)

    #delete duplicates categories
    df_categories.drop_duplicates(keep = 'first', inplace=True)
    #Add a new column to this df to determinate if this categorie can take as a restautant
    df_categories["isRestaurant"] = np.nan
    # Save this file as csv
    df_categories.to_csv("categorie.csv")
    #print(df_categories)
    return df_categories


def common_items(list1, list2):
    list1_set = set(list1)
    list2_set = set(list2)
    if (list1_set & list2_set):
        return True
    else:
        return False

# Prend en paramétere le df des business et retourn les commerces "Restaurants"
#En se basant sur la liste des catégories filtrées.
def get_restaurant_categories(df):
    df_filtred_categories = pd.read_csv("filtred_categories.csv", delimiter=";", header=0, low_memory=False)
    df_selected_categories = df_filtred_categories[df_filtred_categories["isRestaurant"] == 1]
    list_selected_categories = df_selected_categories['Categorie'].values.tolist()
    #print(list_selected_categories)
    i = 0

    df["isRestaurant"] = np.nan

    for idx, row in df.iterrows():
        categorie = df.loc[idx,'categories']
        if(pd.notnull(categorie)):
            list_categorie = categorie.split(',')
            if(common_items(list_categorie,list_selected_categories)):
                df.loc[idx,'isRestaurant'] = True
            else:
                df.loc[idx,'isRestaurant'] = False
    return df

def get_categories_Analyis(df_business):
    df_business = df_business[df_business['categories'].notna()]

    categories = ';'.join(df_business['categories'])
    all_categories = re.split(';|,', categories)
    bus_cat_trim = [item.lstrip() for item in all_categories]
    print(bus_cat_trim)
    df_bus_cat = pd.DataFrame(bus_cat_trim, columns=['category'])

    bus_cat_count = df_bus_cat.category.value_counts()
    bus_cat_count = bus_cat_count.sort_values(ascending=False)
    bus_cat_count = bus_cat_count.iloc[0:30]

    fig = plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=bus_cat_count.index, y=bus_cat_count.values)
    plt.title("Principales catégories", fontsize=20)
    x_locs, x_labels = plt.xticks()
    plt.setp(x_labels, rotation=90)
    plt.ylabel('Le nombre de business', fontsize=15)
    plt.xlabel('Catégorie', fontsize=15
               )
    plt.show()


def get_restaurants_per_city(df_business):
    df_business = df_business[df_business['city'].notna()]

    cities = df_business['city']
    print(cities)
    df_bus_city = pd.DataFrame(cities, columns=['city'])

    bus_city_count = df_bus_city.city.value_counts()
    bus_city_count = bus_city_count.sort_values(ascending=False)
    bus_city_count = bus_city_count.iloc[0:30]

    fig = plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=bus_city_count.index, y=bus_city_count.values)
    plt.title("Nombre de commerces 'Restaurants' dans chaque ville", fontsize=20)
    x_locs, x_labels = plt.xticks()
    plt.setp(x_labels, rotation=90)
    plt.ylabel('Le nombre de business', fontsize=15)
    plt.xlabel('Ville', fontsize=15
               )
    plt.show()



#df_business = pd.read_csv("../data/csv/restaurants.csv", header=0, low_memory=False)
#get_restaurants_per_city(df_business)
#df_selected_categories = get_restaurant_categories(df_business)