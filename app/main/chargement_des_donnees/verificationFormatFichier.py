#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Module "Vérification format fichier"
	========================================================
"""

from flask import Flask
import os


def verifOuverture(chemin):
	"""
		Fonctionnalité de vérification de l'existance du fichier pour l'ouverture

		:param chemin: chemin du fichier
		:type chemin: str
		:return: entier 0 ou une description de l'erreur
    """  
	if not os.path.isfile(chemin):
		print(os.path.isfile(chemin))
		return "Error: not an existing file"
	return 0

	
def verifExtension(chemin):
	"""
		Fonctionnalité de vérification de l'extension du fichier

		:param chemin: chemin du fichier
		:type chemin: str
		:return: entier 0 ou une description de l'erreur
    """ 
	if os.path.splitext(chemin)[1] != ".csv":
		return "Error: file extension not .csv"
	return 0

	
def verifLecture(fichierCSV):
	"""
		Fonctionnalité de vérification de l'accès au contenu du fichier et de sa nature

		:param fichierCSV: le fichier CSV ouvert
		:type fichierCSV: TextIoWrapper
		:return: entier 0 ou une description de l'erreur
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

	
def ouvrir(chemin):
	"""
		Fonctionnalité principale d'ouverture du fichier CSV et de vérification

		:param chemin: chemin du fichier
		:type chemin: str
		:return: le fichier CSV ouvert ou la description de l'erreur rencontrée lors de l'ouverture
    """
	#test du chemin du fichier
	codeErreur = verifOuverture(chemin)
	if codeErreur != 0: return codeErreur
	
	#test du l'extension sur le chemin du fichier
	codeErreur = verifExtension(chemin)
	if codeErreur != 0: return codeErreur
		
	#ouverture en lecture
	fichierCSV = open(chemin, "r", encoding='utf-8')	
	
	#test de l'accès en lecture
	codeErreur = verifLecture(fichierCSV) 
	if codeErreur != 0: return codeErreur
	
	return fichierCSV
	
