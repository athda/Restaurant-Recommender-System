import pandas as pd


''' STEP 1: Import the csv file in a Dataframe'''
#Import the initial business csv file in a dataFrame
df_tip = pd.read_csv("../../data/csv/tip.csv", header=0, low_memory=False)


''' STEP 2: Remove columns ()'''

''' STEP 3: Delete rows with null values of name file'''
for idx, row in df_tip.iterrows():
    if (pd.isnull(row['text'])):
        print("*******")
        df_tip = df_tip.drop([idx])

''' STEP 4: Save the final datafrmae as a csv file'''
df_tip.to_csv(df_tip.to_csv("../../data/csv/new_tip.csv"))