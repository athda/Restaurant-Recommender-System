import pandas as pd
from business_categories import *
from business_localisation import *

from Data_PreProcessing.business.business_categories import get_restaurant_categories
from Data_PreProcessing.business.business_localisation import compelete_mising_value_address_city_postalCode

''' STEP 1: Import the csv file in a Dataframe'''
#Import the initial business csv file in a dataFrame
df_business = pd.read_csv("../../data/csv/business.csv", header=0, low_memory=False)

''' STEP 2: Remove not important columns (json file attributs)'''
# The "filtred_business_columns_toDelete.txt" we find the columns determined as not important#
#The columns are deleted dependign on this file#
# get the list of columns to be deleted #
columns_toDelete = []
for item in open('./filtred_business_columns_toDelete.txt').readlines():
    columns_toDelete.append(item.strip('\n'))

# get the columns of initial_df_business
df_business_columns = df_business.columns

#get the common elemnts of two lists
common_columns = list(set(df_business_columns).intersection(columns_toDelete))

#drop columns
df_business = df_business.drop(columns=common_columns)


'''*** STEP 3 ***: Delete identify business that are restaurants'''
# The functions used to complete this task are defined in "business_categories.py"
# At the end of this step, we will have a dataframe with a new column "is restaurant"
# determining if a business is a restaurant or not (True the business is a restaurant)

df_business = get_restaurant_categories(df_business)
print(df_business['isRestaurant'].dtype)

df_restaurants = df_business.loc[df_business['isRestaurant'] == True]
print(df_restaurants.shape)



'''*** STEP 4 ***: Complete Missing values of address, postal_code, city'''
df_restaurants = compelete_mising_value_address_city_postalCode(df_restaurants)


df_restaurants.to_csv("../../data/csv/restaurants.csv")


