#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from add.intervalle import Intervalle
from add.addQualitatives import calculEffectifs, calculEffectifsCumules, calculFrequences, calculFrequencesCumulees
import os

def moyenne(listeEffectifs):
	"""Calcule la moyenne arithmétique.
	
	:param listeEffectifs: liste de couples (valeur, occurences)
	:return: moyenne arithmétique des valeurs de la liste
	"""
	resultat, taille = 0, 0
	for couple in listeEffectifs:
		resultat += couple[0] * couple[1]
		taille += couple[1]
	#taille est la somme des effectifs : la taille du jeu de données
	return resultat / taille
	
def quantileDiscret(ordre, listeFrequencesCumulees):
	"""
        Calcule le quantile d'ordre ``ordre``.
        
	Quantile non défini si l'ordre n'est pas compris entre 0 exclus et 1 exclus
	
	:param ordre: Nombre flottant compris entre 0 et 1.
	:param listeFrequencesCumulees: liste de couples (valeur, frequence cumulée) triée selon les valeurs 
	:return: La première valeur telle que la fréquence cumulée correspondante soit supérieure ou égale à l'ordre.
	:rtype: float
	
	.. note::
		La médiane est le quantile d'ordre 0.5.
		
		Les quartiles sont les quantiles d'ordre 0.25 et 0.75.
	"""
	if ordre >= 1 or ordre <= 0:
		return float('nan')
	
	i = 0
	while listeFrequencesCumulees[i][1] < ordre:
		i += 1
		
	#A la sortie de la boucle listeFrequencesCumulees[i][1] >= ordre
	return listeFrequencesCumulees[i][0]
	
def variance(listeEffectifs):
	"""Calcule la variance.
	
	La variance représente statistiquement l'écart quadratique à la moyenne.
	
	Plus les valeurs du eu de données sont proches de la moyenn, plus la variance est faible.
	
	:param listeEffectifs: liste de couples (valeur, occurences)
	:rtype: float
	"""
	
	moy = moyenne(listeEffectifs)
	resultat, taille = 0, 0
	for couple in listeEffectifs:
		resultat += ((couple[0] - moy) ** 2) * couple[1]
		taille += couple[1]
	
	return resultat / taille
	
def ecartType(variance):
	"""Calcule l'écart-type.
	
	L'écart-type est la racine carrée de la variance.
	
	Cette statistique permet de justifier la pertinence ou non de la valeur moyenne.
	
	:rtype: float
	"""
	return sqrt(variance)
	
def anomaliesTukeyDiscret(listeEffectifs):
	"""Liste les valeurs aberrantes de la list, cas discret.
	
	Une valeur est dite aberrante selon la règle de Tukey si elle n'appartient pas à un intervalle I définit tel que :
	I = [Q1 - k * IQ ; Q3 + k * IQ] , k constante réelle Q1 et Q3 les quartiles, IQ l'écart inter-quartiles.
	
	La constante k est choisie arbitrairement égale à 1,5. La valeur 1.5 est selon Tukey une valeur pragmatique, qui a une raison probabiliste.
	Si une variable suit une distribution normale, alors la zone délimitée par la boîte et les moustaches devrait contenir 99,3 % des observations.
	
	:rtype: list
	:return: Collection contenant les données anormales pour la distribution des valeurs.
	"""
	listeFrequencesCumulees = calculFrequencesCumulees(calculEffectifsCumules(listeEffectifs))
	q1 = quantileDiscret(0.25, listeFrequencesCumulees)
	q3 = quantileDiscret(0.75, listeFrequencesCumulees)
	iq = q3 - q1
	interv = Intervalle(q1 - 1.5 * iq, q3 + 1.5 * iq, True, True)
	listeAnomalies = []
	for couple in listeEffectifs:
		if not interv.contient(couple[0]):
			for i in range(couple[1]):
				listeAnomalies.append(couple[0])
	#On ajoute la valeur dans resultat autant de fois qu'elle est présente dans la série.
	return listeAnomalies

def symetrie(listeEffectifs):
	"""Calcule le coefficient de symétrie de Fisher.
	
		Si le coefficient est proche 0, la distribution est approximativement symétrique.
	
		Si le coefficient est positif, la distribution est étalée sur la droite.
	
		Si le coefficient est négatif, la distribution est étalée sur la gauche.
	
	En théorie si l'écart-type est égal à 0, la symétrie n'est pas définie.
	
	Cependant un écart-type égal à 0 s'interprète :
	
		Si toutes les valeurs de la distribution sont égales à la moyenne, notre écart-type va être nul.
		
		On peut alors considérer la distribution parfaitement symétrique, toutes les données sont regroupées en un point, la moyenne.
	
	:rtype: float
		
	"""
	moy = moyenne(listeEffectifs)
	
	somme, taille = 0, 0
	for couple in listeEffectifs:
		somme += ((couple[0] - moy) ** 3) * couple[1]
		taille += couple[1]
		
	momentCentreOrdre3 = somme / taille
	ecType = ecartType(variance(listeEffectifs))
	
	if ecType == 0:
		return 0
	else:	
		return  momentCentreOrdre3 / (ecType ** 3)
	
def aplatissement(listeEffectifs):
	"""Calcule le coefficient d'aplatissement de Fisher.
	
		Si le coefficient est égal à 3, la distribution suit une loi normale centrée réduite.
	
		Si le coefficient est inférieur à 3, la distribution est aplatie.
	
		Si le coefficient est supérieur à 3, les valeurs de la distribution est concentrée autour de la moyenne.
	
	Non défini si l'écart-type est nul
	
	:rtype: float
	"""
	moy = moyenne(listeEffectifs)
	
	somme, taille = 0, 0
	for couple in listeEffectifs:
		somme += ((couple[0] - moy) ** 4) * couple[1]
		taille += couple[1]
		
	momentCentreOrdre4 = somme / taille
	ecType = ecartType(variance(listeEffectifs))
	
	if ecType == 0:
		return float('nan')
	else:
		return  momentCentreOrdre4 / (ecType ** 4)

def infoDistribution(listeEffectifs):
	"""Création d'un dictionnaire pour la distribution des données.
	
	Cette fonction est compatible pour les données discrètes et continues.
	
	Couples (clé, valeur):
		* "x" : liste des abscisses, les données
		* "value" : liste des ordonnées, les effectifs cumulés respectifs
	
	:param listeEffectifs: liste de couples (valeur, effectif).
	:rtype: dict
	"""
	
	abscisses = []
	values = []
	for couple in listeEffectifs:
		abscisses.append(couple[0])
		values.append(couple[1])
		
	distribution = {}
	distribution['x'] = abscisses
	distribution['value'] = values
	
	return distribution

def infoDistributionCumulativeDiscrete(listeEffectifsCumules):
	"""Création d'un dictionnaire pour la distribution cumulative des données discrètes.
	
	Couples (clé, valeur):
		* "x" : liste des abscisses, les données
		* "value" : liste des ordonnées, les effectifs cumulés respectifs
		
	:param listeEffectifCumules: liste de couples (valeur, effectif cumulé).
	:rtype: dict
	"""
	abscisses = []
	values = []
	for couple in listeEffectifsCumules:
		abscisses.append(couple[0])
		values.append(couple[1])
		
	distributionC = {}
	distributionC['x'] = abscisses
	distributionC['value'] = values
	
	return distributionC
	
def infoBoiteTukeyDiscret(listeEffectifs):
	"""Création d'un dictionnaire pour la boîte à moustaches de Tukey, cas discret.
	
	Cette fonction est compatible pour les données discrètes et continues.
	
	Couples (clé, valeur):
		* "q1" : premier quartile
		* "q3" : troisième quartile
		* "median" : la médiane de la série de données
		* "left" : extrémité de la moustache gauche, Q1 - k * (Q3 - Q1)
		* "droite" : extrémité de la moustache droite, Q3 + k * (Q3 - Q1)
		* "outliers" : une liste des anomalies statistiques
	
	:param listeEffectifs: liste de couples (valeur, effectif).
	:rtype: dict
	"""	
	listeFC = calculFrequencesCumulees(calculEffectifsCumules(listeEffectifs))
	q1 = quantileDiscret(0.25, listeFC)
	q3 = quantileDiscret(0.75, listeFC)
	median = quantileDiscret(0.5, listeFC)
	
	tukey = {}
	tukey['q1'] = q1
	tukey['q3'] = q3
	tukey['median'] = median
	tukey['left'] = q1 - 1.5 * (q3 - q1)
	tukey['right'] = q3 + 1.5 * (q3 - q1)
	tukey['outliers'] = anomaliesTukeyDiscret(listeEffectifs)
		
	return tukey
	

