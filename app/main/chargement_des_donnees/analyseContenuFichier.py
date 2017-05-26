#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Analyse Contenu fichier``
	========================================================
"""

import csv, ast, re
from datetime import datetime
#from verificationFormatFichier import ouvrir

def lecture(fichierCSV,toClose):
	"""
		Fonction de lecture du contenu du fichier CSV ligne par ligne

		:param fichierCSV: fichier CSV ouvert et vérifié
		:type fichierCSV: TextIoWrapper
		:return: liste dont chaque élément est une sous-liste contenant les données d’une ligne du fichier
    """ 
	lignesCSV = []
	
	#determination du délimiteur
	text = fichierCSV.read()
	fichierCSV.seek(0)
	delim = csv.Sniffer().sniff(text)
	
	#lecture
	readerCSV = csv.reader(fichierCSV, delim)
	
	#le nombre de colonnes du fichier CSV est connu à partir des noms données aux colonnes, les valeurs sans noms seront ignorées
	#remplissage dans une liste homogène
	firstLine = True
	for ligne in readerCSV:
		if (firstLine):
			nbColonnes = len(ligne)
			firstLine = False
		while len(ligne) > nbColonnes:
			ligne.pop()
		while len(ligne) < nbColonnes:
			ligne.append('')
		lignesCSV.append(ligne)
	
	#fermeture du flux (plus besoin)
	if toClose:
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
	
	#noms
	descCSV["nom"] = lignesCSV[0]
	del lignesCSV[0]
	
	#types attendus des données (selon leurs noms)
	descCSV["type"] = []
	for nom in descCSV["nom"]:
		if "time" in nom.lower() or "temps" in nom.lower() or "date" in nom.lower():
			descCSV["type"].append("date")
		elif "parent" in nom.lower() or "root" in nom.lower() or "racine" in nom.lower():
			descCSV["type"].append("parent")
		elif "enfant" in nom.lower() or "child" in nom.lower():
			descCSV["type"].append("enfant")
		else: descCSV["type"].append("nombre")
	
	#recherche des erreurs : comparaison du type attendu avec le type actuel
	descCSV["erreurs"] = []
	
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
						descCSV["erreurs"][numLigne][numColonne] = "date string error"
					except IndexError:
						descCSV["erreurs"][numLigne][numColonne] = "date string error"
				elif typeDeDonnee(donnee) == "VIDE":
					descCSV["erreurs"][numLigne][numColonne] = "missing value"
					
			elif  descCSV["type"][numColonne] == "enfant" or descCSV["type"][numColonne] == "parent":
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
	lignesCSV = lecture(fichierCSV,True)
	
	descCSV = descriptionColonnes(lignesCSV)
		
	return lignesCSV, descCSV
	
	
#test independant du module (import à vérifier avant)
if __name__ == "__main__":
	
	#JD : il faut appeler la fct ouvrir, voir s'il y'a erreur et ensuite appeler la fct analyse et me renvoyer son résultat
	#le problème si je prends juste le chemin pour la fct analyse et que j'ouvre le fichier dedans c'est que tu ne pourras pas faire grand chose avec le message d'erreur
	
	fichierCSV = ouvrir("test.csv")
	
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
