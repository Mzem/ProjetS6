#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, ast, re
from datetime import datetime
from chargement_des_donnees.verificationFormatFichier import ouvrir

def lecture(fichierCSV,toClose):
	"""Lit le contenu du fichier CSV ligne par ligne.
	
	Lors du parcours du fichier ``fichierCSV``, la fonction se charge de remplir une structure contenant les données du fichier.

	:param fichierCSV: fichier CSV ouvert et vérifié
	:type fichierCSV: TextIoWrapper
	:return: liste dont chaque élément est une sous-liste contenant les données d’une ligne du fichier.
    """ 
	lignesCSV = []
	
	#determination du délimiteur
	text = fichierCSV.read()
	fichierCSV.seek(0)
	delim = csv.Sniffer().sniff(text)
	
	#lecture
	readerCSV = csv.reader(fichierCSV, delim)
	
	#le nombre de colonnes du fichier CSV est connu à partir des noms donnés aux colonnes, les valeurs sans nom seront ignorées
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
	"""Détecte le type des données depuis une chaine de caractères.

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
	"""Supprime les suffixes des jours du mois dans une chaine de caractères représentant une date
	
	:param chaineDate: chaine de caractères représentant une date
	:type lignesCSV: str
	:return: chaine de caractères de la date sans suffixes
	"""
	parts = chaineDate.split()
	parts[1] = parts[1].strip("stndrh")
	return " ".join(parts)
	
def descriptionColonnes(lignesCSV):
	"""Renseignement des descriptions du nom, du type et des erreurs des colonnes du fichier CSV.
	
	On va enregistrer dans un dictionnaire ``descCSV`` des informations concernant :
	
	* Le nom des colonnes.
	* Le type attendu pour chacune des colonnes.
	* Un mention d'erreur ou ``correct`` pour chaque donnée du fichier par rapport au type attendu.

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
	"""Fonctionnalité principale d'analyse du contenu du fichier CSV ouvert.
	
	Cette fonctionnalité réutilise deux fonctions, ``lecture`` et ``descriptionColonnes``.
	
	Objectifs:
		* Lire les données présentes dans le fichier ``.csv``.
		* Fournir un description de ce fichier : nom des colonnes, type des données, erreurs relevées.

	:param fichierCSV: le fichier CSV ouvert et vérifié
	:type fichierCSV: TextIoWrapper
	:return: un couple (données du fichier, description de ces données)
    """
	lignesCSV = lecture(fichierCSV,True)
	descCSV = descriptionColonnes(lignesCSV)
		
	return lignesCSV, descCSV
