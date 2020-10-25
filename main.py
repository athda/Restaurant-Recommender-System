# ce script va nous permettre de des imbriquer les données
# importation des librairies
import pandas as pd
import fonctions
if __name__ == "__main__":
	df = pd.read_csv('data/csv/business.csv', header=0,low_memory=False)