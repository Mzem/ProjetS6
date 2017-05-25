#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Analyse de données quantitatives discrètes``
	========================================================
	
	
"""

from math import sqrt
from add.intervalle import Intervalle
from add.addQualitatives import calculFrequences, calculFrequencesCumulees
import os

def moyenne(listeEffectifs):
	"""
        Calcule la moyenne arithmétique.
	
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
	:param listeFrequencesCumulees: liste de couples (valeur, frequence cumulee) triée selon les valeurs 
	:return: La première valeur telle que la fréquence cumulée correspondante soit supérieure ou égale à l'ordre.
	:rtype: float
	
	.. note:: La médiane est le quantile d'ordre 1/2. Les quartiles sont les quantiles d'ordre 1/4 et 3/4.
	"""
	
	if ordre >= 1 or ordre <= 0:
		return float('nan')
	
	i = 0
	while listeFrequencesCumulees[i][1] < ordre:
		i += 1
		
	#A la sortie de la boucle listeFrequencesCumulees[i][1] >= ordre
	return listeFrequencesCumulees[i][0]
	
def variance(listeEffectifs):
	"""
        Calcule la variance.
        """
	
	moy = moyenne(listeEffectifs)
	resultat, taille = 0, 0
	for couple in listeEffectifs:
		resultat += ((couple[0] - moy) ** 2) * couple[1]
		taille += couple[1]
	
	return resultat / taille
	
def ecartType(variance):
	"""Calcule l'écart-type."""
	
	return sqrt(variance)
	
def anomaliesTukey(listeEffectifs):
	"""
        Liste les valeurs aberrantes de la liste.
	
	Une valeur est dite aberrante selon la règle de Tukey si elle n'appartient pas à un intervalle I définit tel que :
	I = [Q1 - k * IQ ; Q3 + k * IQ] , k constante réelle Q1 et Q3 les quartiles, IQ l'écart inter-quartiles.
	
	La constante k est choisie arbitrairement égale à 1,5. La valeur 1.5 est selon Tukey une valeur pragmatique, qui a une raison probabiliste.
	Si une variable suit une distribution normale, alors la zone délimitée par la boîte et les moustaches devrait contenir 99,3 % des observations.
	
	:rtype: list
	:return: Collection contenant les données anormales pour la distribution des valeurs.
	
	"""
	listeFrequencesCumulees = calculFrequencesCumulees(calculFrequences(listeEffectifs))
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
	"""
        Calcule le coefficient de symétrie de Fisher.
	
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
	"""
        Calcule le coefficient d'aplatissement de Fisher.
	
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

def infoDistributionDiscrete(listeEffectifs):
	"""
        Écriture dans le fichier distribution.js
	
	Format du fihier :
		Début
		{
			"x": [ liste des abscisses ],
			"value": [ liste des ordonnées / effectifs ]
		}
		Fin
		
	:param listeEffectifs: liste de couples (valeur, effectif).
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
	"""
        Écriture dans le fichier distributionCumulative.js
	
	Format du fihier :
		Début
		{
			"x": [ liste des abscisses ],
			"value": [ liste des ordonnées / effectifs cumulés ]
		}
		Fin
		
	:param listeEffectifCumules: liste de couples (valeur, effectif cumulé).
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
	
def infoBoiteTukey(listeEffectifs):
	"""
        Écriture dans le fichier boxplot.js
	
	Format du fihier :
		Début
		{
			"q1": premier quartile,
			"median": mediane,
			"q3": troisième quartile,
			"left": extrémité gauche de la moustache (q1 - 1.5*(q3-q1)),
			"right": extrémité droite de la moustache (q3 + 1.5*(q3-q1)),
			"outliers": liste des anomalies statistiques
		}
		Fin
		
	Informations utiles à la création d'une boîte à moustaches de Tukey
		
	:param listeEffectifs: liste de couples (valeur, effectif).
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
	tukey['outliers'] = anomaliesTukey(listeEffectifs)
		
	return tukey

def infoSerieTemporelle(listeSerieTemporelle):
	"""
        Écriture dans le fichier timeSeries.js
	
	Format du fihier :
		Début
		{
			"x": [ liste des Timestamp ],
			"value": [ liste des valeurs ]
		}
		Fin
		
	:param listeSerieTemporelle: liste de couples (Timestamp, valeur), et un Timestamp est une chaîne de caractères.
	"""
	timestamps = []
	values = []
	for couple in listeSerieTemporelle:
		timestamps.append(couple[0])
		values.append(couple[1])
		
	timeSeries = {}
	timeSeries['x'] = timestamps
	timeSeries['value'] = values
	
	return timeSeries

