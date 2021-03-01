import pandas as pd
import geopy


df_business = pd.read_csv("../../data/csv/business.csv", header=0, low_memory=False)
geolocator = geopy.Nominatim(user_agent='Restaurant-Recommender-System', timeout=10)


def get_postal_code(latitude, longitude):
    location = geolocator.reverse((latitude, longitude))
    if "postcode" in location.raw['address'].keys():
        return location.raw['address']['postcode']


def get_address(latitude,longitude):
    location = geolocator.reverse((latitude, longitude))
    return str(location)

def get_city(latitude,longitude):
    location = geolocator.reverse((latitude, longitude))
    if "city" in location.raw['address'].keys():
        return location.raw['address']['city']


def compelete_mising_value_address_city_postalCode(df):
    i=0
    j=0
    k=0
    for idx, row in df.iterrows():
        lat = df.loc[idx, 'latitude']
        lon = df.loc[idx, 'longitude']
        if(pd.isnull(row['postal_code'])):
            i = i+1
            print("i",i)
            df.loc[idx, 'postal_code'] = get_postal_code(lat, lon)
        if (pd.isnull(row['address'])):
            j = j + 1
            print("j", j)
            df.loc[idx, 'address'] = get_address(lat, lon)
        if (pd.isnull(row['city'])):
            k = k + 1
            print("k", k)
            df.loc[idx, 'city'] = get_city(lat, lon)

    return df

#df_business.to_csv("../data/csv/new_business_1.csv")