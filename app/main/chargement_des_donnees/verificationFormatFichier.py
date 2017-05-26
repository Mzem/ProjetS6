#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, csv

def verifExistence(chemin):
	"""Vérifie l'existance du fichier pour l'ouverture.

	:param chemin: chemin du fichier
	:type chemin: str
	:return: entier 0 ou une erreur ``not an existing file``
	"""  
	if not os.path.isfile(chemin):
		print(os.path.isfile(chemin))
		return "Error: not an existing file"
	return 0

	
def verifExtension(chemin):
	"""Vérification l'extension du fichier.

	:param chemin: chemin du fichier
	:type chemin: str
	:return: entier 0 ou une erreur ``file extension not .csv``
    """ 
	if os.path.splitext(chemin)[1] != ".csv":
		return "Error: file extension not .csv"
	return 0

	
def verifLecture(fichierCSV):
	"""Vérifie l'accès au contenu du fichier ainsi que sa nature.

	:param fichierCSV: le fichier CSV ouvert
	:type fichierCSV: TextIoWrapper
	:return: entier 0, une erreur ``not a raw text file`` ou ``file content not readable``
    """ 
	if not fichierCSV.readable():
		return "Error: file content not readable"
	
	#test du contenu du fichier (si c'est bien du texte non formaté)
	try:
		fichierCSV.read()
		fichierCSV.seek(0)	#remise du curseur au début
	except UnicodeDecodeError:
		return "Error: not a raw text file"
	
	return 0

	
def verifCSV(fichierCSV):
	"""Vérifie si le fichier CSV présumé est strucutré.
	
	Examine si le fichier contient bien un caractère délimitant les valeurs entre elles.

	:param fichierCSV: le fichier CSV ouvert
	:type fichierCSV: TextIoWrapper
	:return: entier 0 ou une erreur ``not a structured CSV file``
    """ 
	text = fichierCSV.read()
	fichierCSV.seek(0)
	try:
		csv.Sniffer().sniff(text)
	except csv.Error:
		return "Error: not a structured CSV file"
		
	return 0
	
def ouvrir(chemin):
	"""Fonctionnalité principale d'ouverture du fichier CSV et de vérification

	:param chemin: chemin du fichier
	:type chemin: str
	:return: le fichier CSV ouvert ou la description de l'erreur rencontrée lors de l'ouverture
    """
	#test du chemin du fichier
	codeErreur = verifExistence(chemin)
	if codeErreur != 0: return codeErreur
	
	#test du l'extension sur le chemin du fichier
	codeErreur = verifExtension(chemin)
	if codeErreur != 0: return codeErreur
		
	#ouverture en lecture
	fichierCSV = open(chemin, "r", encoding='utf-8')	
	
	#test de l'accès en lecture
	codeErreur = verifLecture(fichierCSV) 
	if codeErreur != 0: 
		fichierCSV.close()
		return codeErreur	
		
	#test de la strucutre du fichier
	codeErreur = verifCSV(fichierCSV) 
	if codeErreur != 0: 
		fichierCSV.close()
		return codeErreur
	
	return fichierCSV
