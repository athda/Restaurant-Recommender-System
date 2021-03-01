import pandas as pd


''' STEP 1: Import the csv file in a Dataframe'''
#Import the initial business csv file in a dataFrame
df_user = pd.read_csv("../../data/csv/user.csv", header=0, low_memory=False)


''' STEP 2: Remove columns (json file attributs)'''
columns_toDelete = ['elite']
#drop columns
df_user = df_user.drop(columns=columns_toDelete)
print(df_user)
print(df_user.columns)

print(df_user.shape)
''' STEP 3: Delete rows with null values of name file'''
for idx, row in df_user.iterrows():
    if (pd.isnull(row['name'])):
        print("*******")
        df_user = df_user.drop([idx])

''' STEP 4: Save the final datafrmae as a csv file'''
df_user.to_csv(df_user.to_csv("../../data/csv/new_user.csv"))
