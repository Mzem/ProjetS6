#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Module "Analyse Contenu fichier"
	========================================================
"""

import csv, ast, re
from datetime import datetime
#from verificationFormatFichier import ouvrir


def lecture(fichierCSV):
	"""
		Fonction de lecture du contenu du fichier CSV ligne par ligne

		:param fichierCSV: fichier CSV ouvert et vérifié
		:type fichierCSV: TextIoWrapper
		:return: liste dont chaque élément est une sous-liste contenant les données d’une ligne du fichier
    """ 
	lignesCSV = []
	
	#lecture
	readerCSV = csv.reader(fichierCSV, delimiter=",")
	
	#remplissage dans une liste
	for ligne in readerCSV:
		lignesCSV.append(ligne)
	
	#fermeture du flux (plus besoin)	
	fichierCSV.close()
	
	return lignesCSV

	
def typeDeDonnee(chaine):
	"""
		Fonction de detection du type de donnée depuis une chaine de carcteres

		:param fichierCSV: fichier CSV
		:type fichierCSV: TextIoWrapper
		:return: liste dont chaque élément est une sous-liste contenant les données d’une ligne du fichier
    """ 
	#retrait des caractères blancs du début et de la fin de la donnée
	chaine = chaine.strip()
	
	#test des différentes possibilités pour une donnée
	if len(chaine) == 0: return 'VIDE'
	try:
		#évaluation et récupération du type de la donnée
		t = ast.literal_eval(chaine)
	except ValueError:
		return 'TEXTE'
	except SyntaxError:
		return 'TEXTE'
	else:
		if type(t) in [int, float, bool]:
			if type(t) is bool:
				return 'BOOL'
			if type(t) is int:
				return 'ENTIER'
			if type(t) is float:
				return 'REEL'
		else:
			return 'TEXTE'
	
	
def removeDateSuffix(chaineDate):
    parts = chaineDate.split()
    parts[1] = parts[1].strip("stndrh")
    return " ".join(parts)
	
def descriptionColonnes(lignesCSV):
	"""
		Fonction de description du nom, du type et des erreurs des colonnes du fichier CSV

		:param lignesCSV: lignes du fichier CSV
		:type lignesCSV: list
		:return: dictionnaire de 3 sous-listes ayant pour clés : "nom", "type" et "erreurs"
    """ 
	descCSV = {}
	descCSV["nom"] = lignesCSV[0]
	del lignesCSV[0]
	descCSV["type"] = ["date","entier","entier","nombre","nombre","nombre","nombre"]
	#initialisation d'une liste contenant les descriptions des erreurs avec la meme taille que la liste représentant le fichier
	descCSV["erreurs"] = []
	
	#recherche des erreurs : comparaison du type attendu avec le type actuel
	numLigne = 0
	for ligne in lignesCSV:
		descCSV["erreurs"].append([])	#rajoute une ligne dans la liste d'erreurs
		numColonne = 0
		
		for donnee in ligne:
			descCSV["erreurs"][numLigne].append("type error")	#rajoute une colonne dans cette ligne de la liste d'erreurs
			t = typeDeDonnee(donnee)
			
			#Gestion des données de type date
			if  descCSV["type"][numColonne] == "date":
				if t == "TEXTE": 
					try:
						date = datetime.strptime(removeDateSuffix(donnee),'%B %d %Y, %H:%M:%S.%f')
						lignesCSV[numLigne][numColonne] = date
						descCSV["erreurs"][numLigne][numColonne] = "correct"
					except ValueError:
						descCSV["erreurs"][numLigne][numColonne] = "date string format not supported"
					except IndexError:
						descCSV["erreurs"][numLigne][numColonne] = "date string format not supported"
				elif typeDeDonnee(donnee) == "VIDE":
					descCSV["erreurs"][numLigne][numColonne] = "missing value"
					
			elif  descCSV["type"][numColonne] == "entier":
				if t == "ENTIER": 
					descCSV["erreurs"][numLigne][numColonne] = "correct"
					lignesCSV[numLigne][numColonne] = int(donnee)
				elif t == "VIDE":
					descCSV["erreurs"][numLigne][numColonne] = "missing value"
					
			elif  descCSV["type"][numColonne] == "nombre":
				if t == "ENTIER" or t == "REEL": 
					descCSV["erreurs"][numLigne][numColonne] = "correct"
					lignesCSV[numLigne][numColonne] = float(donnee)
				elif t == "VIDE":
					descCSV["erreurs"][numLigne][numColonne] = "missing value"
					
			numColonne+=1
		numLigne+=1
		
	return descCSV
	
	
def analyseFichier(fichierCSV):
	"""
		Fonctionnalité principale d'analyse du contenu du fichier CSV ouvert

		:param fichierCSV: le fichier CSV ouvert et vérifié
		:type fichierCSV: TextIoWrapper
		:return: une liste contenant les données du fichier et un dictionnaire décrivant ces données
    """
	lignesCSV = lecture(fichierCSV)
	
	descCSV = descriptionColonnes(lignesCSV)
		
	return lignesCSV, descCSV
	
	
#test independant du module
if __name__ == "__main__":
	
	#JD : il faut appeler la fct ouvrir, voir s'il y'a erreur et ensuite appeler la fct analyse et me renvoyer son résultat
	#le problème si je prends juste le chemin pour la fct analyse et que j'ouvre le fichier dedans c'est que tu ne pourras pas faire grand chose avec le message d'erreur
	
	fichierCSV = ouvrir("fichier topologie csv st denis.csv")
	
	if type(fichierCSV) is str: 
		print(fichierCSV)
	else :
		lignesCSV, descCSV = analyseFichier(fichierCSV)
	
		#Affichages de test
		print("\n###################################################################################\n")
		
		for ligne in lignesCSV:
			print(ligne)
		
		print("\n###################################################################################\n")
		
		print(descCSV["nom"])
		print(descCSV["type"])
		for ligne in descCSV["erreurs"]:
			print(ligne)
