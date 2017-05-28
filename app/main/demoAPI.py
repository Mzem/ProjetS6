 #!/usr/bin/env python
# -*- coding: utf-8 -*-

from chargement_des_donnees.verificationFormatFichier import ouvrir
from chargement_des_donnees.analyseContenuFichier import *

from add.addQualitatives import *
from add.addQuantitativesDiscretes import moyenne, ecartType, variance
from add.addQuantitativesContinues import discretisation, calculNombreClasses, preparationIntervallesAnalyse, quantileContinu

import sys, csv, errno
from math import sin, log

def mkdir_p(path):
	try:
		os.makedirs(path)
	except OSError as exc:
		if exc.errno == errno.EEXIST and os.path.isdir(path):
			pass
		else: raise

def safe_open_w(path):
	"""
	Ouverture du fichier en écriture et création des dossiers du chemin s'ils n'existent pas.
	"""
	mkdir_p(os.path.dirname(path))
	return open(path, 'w')

def ligneOK(tab, i):
	for verif in tab[i]:
		if verif != "correct":
			return False
	return True
	
def routineAdd(donneesContinues):
	donneesIntervalles, etendueIntervalles = discretisation(calculNombreClasses(donneesContinues), donneesContinues)
	donneesPretes = preparationIntervallesAnalyse(donneesIntervalles)
	
	listeEffectifs = calculEffectifs(donneesPretes)
	listeFrequencesCumulees = calculFrequencesCumulees(calculFrequences(listeEffectifs))
	
	
	minimum = min(donneesContinues)
	maximum = max(donneesContinues)
	etendue = maximum - minimum
	moy = moyenne(listeEffectifs)
	ecart_type = ecartType(variance(listeEffectifs))
	mediane = quantileContinu(0.5, listeFrequencesCumulees, etendueIntervalles)
	iqr = quantileContinu(0.75, listeFrequencesCumulees, etendueIntervalles) - quantileContinu(0.25, listeFrequencesCumulees, etendueIntervalles)
	
	return minimum, maximum, etendue, moy, ecart_type, mediane, iqr

def ecrireResultats(entree, sortie):
	"""Analyses descriptives sur le fichier au chemin ``entree`` écriture des résultats dans ``sortie``
	
	Cette fonction reprend les fonctionnalités de l'API chargement des données pour ouvrir un fichier ``.csv`` et obtenir son contenu ainsi qu'une description des données.
	
	La description des données est utilisée pour réaliser les analyses descriptives uniquement sur les données valides.
	"""
	fichierCSV = ouvrir(entree)
	
	if type(fichierCSV) is str: 
		return fichierCSV #erreur
		
	lignesCSV, descCSV = analyseFichier(fichierCSV)
	donneesStats = {}
	i = 0
	for ligne in lignesCSV:
		if ligneOK(descCSV["erreurs"], i):
			noeud = (ligne[1], ligne[2])
			if noeud not in donneesStats:
				donneesStats[noeud] = {}
				#s'il n'existe pas on l'initialise
				for nomColonne in descCSV["nom"][3:]:
					#liste vide pour chaque cle ayant comme valeur le nom d'une colonne de donnees
					donneesStats[noeud][nomColonne] = []
			else:
				j = 3
				for nomColonne in descCSV["nom"][3:]:
					donneesStats[noeud][nomColonne].append(ligne[j])
					j += 1
		i += 1
			
	with safe_open_w(sortie) as csvfile:
		fichier = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		#Header du csv : "Stats", "Enfant", "Parent", descCSV["nom"]
		fichier.writerow(["stats", "enfant", "parent"] + descCSV["nom"][3:])
		for noeud in donneesStats:
			minimumCol = [] #liste contenant la valeur trouvee pour chaque colonne du csv
			maximumCol = []
			etendueCol = []
			moyenneCol = []
			ecart_typeCol = []
			medianeCol = []
			iqrCol = []
			for nomColonne in donneesStats[noeud]:
				m, M , r, moy, e, med, iqr = routineAdd(donneesStats[noeud][nomColonne])
				minimumCol.append(m)
				maximumCol.append(M)
				etendueCol.append(r)
				moyenneCol.append(moy)
				ecart_typeCol.append(e)
				medianeCol.append(med)
				iqrCol.append(iqr)
			fichier.writerow(["min"]	+ [noeud[0], noeud[1]] + minimumCol)	
			fichier.writerow(["max"]	+ [noeud[0], noeud[1]] + maximumCol)
			fichier.writerow(["range"]	+ [noeud[0], noeud[1]] + etendueCol)
			fichier.writerow(["mean"]	+ [noeud[0], noeud[1]] + moyenneCol)	
			fichier.writerow(["median"]	+ [noeud[0], noeud[1]] + medianeCol)	
			fichier.writerow(["IQR"]	+ [noeud[0], noeud[1]] + iqrCol)	
			fichier.writerow(["stdDev"]	+ [noeud[0], noeud[1]] + ecart_typeCol)	
		
if __name__ == "__main__":
	ecrireResultats(sys.argv[1], sys.argv[2])
