# ce script va nous permettre de des imbriquer les données
# importation des librairies

import fonctions
if __name__ == "__main__":
	fonctions.des_imbriquer("data/json/business.json","data/csv/test.csv",1,100)
	print(fonctions.count_file_lines("data/json/tip.json"))
