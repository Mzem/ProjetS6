"""
	Module "Vérification format fichier"
	========================================================
"""

from flask import Flask
import os

def verifOuverture(chemin):
	"""
		Fonctionnalité de vérification de l’existance du fichier pour l'ouverture

		:param fichierCSV: chemin du fichier
		:type fichierCSV: str
		:return: entier 0 ou code de l'erreur
    """  
	if not os.path.isfile(chemin):
		return "Error: not an existing file"
	return 0

def verifExtension(chemin):
	"""
		Fonctionnalité de vérification de l’extension du fichier

		:param fichierCSV: chemin du fichier
		:type fichierCSV: str
		:return: entier 0 ou code de l'erreur
    """ 
	if os.path.splitext(chemin)[1] != ".csv":
		return "Error: file extension not .csv"
	return 0

def verifLecture(fichierCSV):
	"""
		Fonctionnalité de vérification de l’accès au contenu du fichier et de sa nature

		:param fichierCSV: fichier CSV
		:type fichierCSV: TextIoWrapper
		:return: entier 0 ou code de l'erreur
    """ 
	if not fichierCSV.readable():
		return "Error: file content not readable"
	
	#test du contenu du fichier (si c'est bien du texte non formaté)
	try:
		fichierCSV.read()
	except UnicodeDecodeError:
		return "Error: not a raw text file"
	
	return 0

def ouvrir(chemin):
	"""
		Fonctionnalité principale d'ouverture du fichier CSV et de vérification

		:param fichierCSV: chemin du fichier
		:type fichierCSV: str
		:return: chaîne de caractères signalant le succès ou la description de l'erreur
    """
	#test du chemin du fichier
	codeErreur = verifOuverture(chemin)
	if codeErreur != 0: return codeErreur
	
	#test du l'extension sur le chemin du fichier
	codeErreur = verifExtension(chemin)
	if codeErreur != 0: return codeErreur
		
	#ouverture en lecture
	fichierCSV = open(chemin, "r")	
	
	#test de l'accès en lecture
	codeErreur = verifLecture(fichierCSV)
	if codeErreur != 0: return codeErreur
	
	return "Success opening file"

	
	
#test independant du module
if __name__ == "__main__":
	print(ouvrir("sample.csv"))
	
