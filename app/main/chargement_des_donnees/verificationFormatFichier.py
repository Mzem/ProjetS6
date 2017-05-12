#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Module "VÃ©rification format fichier"
	========================================================
"""

from flask import Flask
import os

def verifOuverture(chemin):
	"""
		FonctionnalitÃ© de vÃ©rification de lâ€™existance du fichier pour l'ouverture

		:param chemin: chemin du fichier
		:type chemin: str
		:return: entier 0 ou code de l'erreur
    """  
	if not os.path.isfile(chemin):
		print(os.path.isfile(chemin))
		return "Error: not an existing file"
	return 0

def verifExtension(chemin):
	"""
		FonctionnalitÃ© de vÃ©rification de lâ€™extension du fichier

		:param chemin: chemin du fichier
		:type chemin: str
		:return: entier 0 ou code de l'erreur
    """ 
	if os.path.splitext(chemin)[1] != ".csv":
		return "Error: file extension not .csv"
	return 0

def verifLecture(fichierCSV):
	"""
		FonctionnalitÃ© de vÃ©rification de lâ€™accÃ¨s au contenu du fichier et de sa nature

		:param fichierCSV: fichier CSV
		:type fichierCSV: TextIoWrapper
		:return: entier 0 ou code de l'erreur
    """ 
	if not fichierCSV.readable():
		return "Error: file content not readable"
	
	#test du contenu du fichier (si c'est bien du texte non formatÃ©)
	try:
		fichierCSV.read()
		fichierCSV.seek(0)	#remise du curseur au dÃ©but
	except UnicodeDecodeError:
		return "Error: not a raw text file"
	
	return 0

def ouvrir(chemin):
	"""
		FonctionnalitÃ© principale d'ouverture du fichier CSV et de vÃ©rification

		:param chemin: chemin du fichier
		:type chemin: str
		:return: chaÃ®ne de caractÃ¨res signalant le succÃ¨s ou la description de l'erreur
    """
	#test du chemin du fichier
	codeErreur = verifOuverture(chemin)
	if codeErreur != 0: return codeErreur
	
	#test du l'extension sur le chemin du fichier
	codeErreur = verifExtension(chemin)
	if codeErreur != 0: return codeErreur
		
	#ouverture en lecture
	fichierCSV = open(chemin, "r", encoding='utf-8')	
	
	#test de l'accÃ¨s en lecture
	codeErreur = verifLecture(fichierCSV) 
	if codeErreur != 0: return codeErreur
	
	return fichierCSV

	
	
#test independant du module
if __name__ == "__main__":
	
	print(ouvrir("fichier_csv_st_denis.csv"))
	
