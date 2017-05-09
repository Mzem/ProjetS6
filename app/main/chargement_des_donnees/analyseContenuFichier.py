#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Module "Vérification format fichier"
	========================================================
"""

from flask import Flask
import csv, ast, re

#fonction (interne) de detection du type de donnée depuis une chaine de carcteres
def typeDeDonnee(chaine):
    chaine = chaine.strip()	#retrait des dechets
    if len(chaine) == 0: return 'VIDE'
    try:
        t = ast.literal_eval(chaine)	#evaluation du type
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


def lecture(fichierCSV):
	"""
		Fonction de lecture du contenu du fichier CSV

		:param fichierCSV: fichier CSV
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
	descCSV["erreurs"] = lignesCSV
	
	#recherche des erreurs : comparaison du type attendu avec le type actuel
	numLigne = 0
	for ligne in lignesCSV:
		numColonne = 0
		for donnee in ligne:
			if  descCSV["type"][numColonne] == "date":
				if typeDeDonnee(donnee) == "TEXTE": 
					descCSV["erreurs"][numLigne][numColonne] = "correct"
				else: 
					descCSV["erreurs"][numLigne][numColonne] = "type error"			
			elif  descCSV["type"][numColonne] == "entier":
				if typeDeDonnee(donnee) == "ENTIER": 
					descCSV["erreurs"][numLigne][numColonne] = "correct"
				elif typeDeDonnee(donnee) == "VIDE":
					descCSV["erreurs"][numLigne][numColonne] = "missing value"
				else: 
					descCSV["erreurs"][numLigne][numColonne] = "type error"			
			elif  descCSV["type"][numColonne] == "nombre":
				if typeDeDonnee(donnee) == "ENTIER" or typeDeDonnee(donnee) == "REEL": 
					descCSV["erreurs"][numLigne][numColonne] = "correct"
				elif typeDeDonnee(donnee) == "VIDE":
					descCSV["erreurs"][numLigne][numColonne] = "missing value"
				else: 
					descCSV["erreurs"][numLigne][numColonne] = "type error"
			numColonne+=1
		numLigne+=1
		
	return descCSV
	
	
#test independant du module
if __name__ == "__main__":
	from verificationFormatFichier import ouvrir
	
	lignesCSV = lecture(ouvrir("sample.csv"))
	for ligne in lignesCSV:
		print(ligne)
	
	print("\n########################\n")
	
	descCSV = descriptionColonnes(lignesCSV)
	print(descCSV["nom"])
	print(descCSV["type"])
	for ligne in descCSV["erreurs"]:
		print(ligne)
	
