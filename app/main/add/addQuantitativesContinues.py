#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import log
from add.intervalle import Intervalle, rechercheIntervalle
from add.addQuantitativesDiscretes import quantileDiscret, moyenne, ecartType, variance
from add.addQualitatives import calculFrequencesCumulees, calculEffectifsCumules
import os

def discretisation(nombreClasses, donneesContinues):
	"""Discrétise des données continues du paramètre ``donneesContinues``.
	
	La fonction se charge de décomposer l’étendue ``[min ; max]`` de l’ensemble de données en ``nombreClasses`` intervalles de même étendue.
	
	Ensuite de remplacer les occurrences des données par l’intervalle auquel la donnée appartient.
	
	:param donneesContinues: liste de nombres flottants
	:return: liste d'intervalles, et étendue discrétisée
	
	"""
	nombreClasses = calculNombreClasses(donneesContinues)
	
	maximum = max(donneesContinues)
	minimum = min(donneesContinues)
	etendue = maximum - minimum
	tailleIntervalle = etendue / nombreClasses
	
	intervalles = []
	for i in range(nombreClasses - 1):
		tmp = Intervalle(minimum + i * tailleIntervalle, minimum + (i + 1) * tailleIntervalle, True, False)
		intervalles.append(tmp)
	
	#dernier intervalle fermé
	tmp = Intervalle(minimum + (nombreClasses - 1) * tailleIntervalle, maximum, True, True)
	intervalles.append(tmp)
	
	listeIntervalles = [None] * len(donneesContinues)
	#remplacement dans donneesContinues la donnee par l'intervalle auquel il appartient
	for i in range(len(donneesContinues)):
		listeIntervalles[i] = rechercheIntervalle(intervalles, donneesContinues[i])
		
	return listeIntervalles, intervalles
	
def calculNombreClasses(donneesContinues):
	"""Calcule le nombre de classes nécessaire à une discrétisation selon la règle de Sturges.
	
	:return: nombre de classes utilisé pour la discrétisation des valeurs
	:rtype: int
	"""
	return 1 + int(log(len(donneesContinues), 2))
	
def preparationIntervallesAnalyse(listeIntervalles):
	"""Prépare les données pour l’utilisation des éléments de calcul du module ``addQuantitativesDiscretes.py``.
	
	Pour effectuer les analyses descriptives dans le cas continu, la démarche est la même (sauf quantiles) que pour le cas discret.
	
	On utilisera cependant comme données les centres des intervalles.
	
	:param listeIntervalles: liste issue de la discrétisation des valeurs.
	:return: liste de flottants.
	
	"""
	
	for i in range(len(listeIntervalles)):
		listeIntervalles[i] = listeIntervalles[i].centre
		
	return listeIntervalles
	
def interpolationLineaire(p1, p2, y):
	"""Calcule l’abscisse par interpolation linéaire
	
	Les points ``p1``, ``p2`` nous permettent de définir une fonction linéaire f(x) = pente * x + ordonnée à l'origine (oo).
	
	On retrouve ensuite l’abscisse du point d’ordonnée ``y`` se trouvant sur la courbe de la fonction, x = (``y`` - oo) / pente.
	
	:return: abscisse de l'ordonnée ``y`` par rapport à la droite (``p1``, ``p2``)
	:rtype: float
	"""
	pente = (p2[1] - p1[1]) / (p2[0] - p1[0])
	oo = p1[1] - pente * p1[0]
	
	return (y - oo) / pente
	
def quantileContinu(ordre, listeFrequencesCumulees, intervalles):
	"""Calcule les quantiles d'ordre ``ordre`` pour une analyse de données conitnues.
	
	Le quantile discret nous permet de retrouver le centre de l'intervalle qui contient le vrai quantile.
	Ensuite, à partir de l'intervalle et de l'ordre, on en déduit une valeur plus précise par interpolation linéaire.
	
	La fonction linéaire est définie à l'aide des bornes de l'intervalle, on  a besoin de deux points :
		
		L'ordonnée de la borne supérieure est la fréquence cumulée du centre de l'intervalle ( 1 si borne = max )
		
		L'ordonnée de la borne inférieur est la fréquence cumulée du centre de l'intervalle précédent ( 0 si borne = min )
	
	:return: le quantile d'ordre ``ordre``
	"""
	centre = quantileDiscret(ordre, listeFrequencesCumulees)
	intervalle = rechercheIntervalle(intervalles, centre)
	
	#recherche des freq cumulees des bornes de l'intervalle
	i = 0
	while centre != listeFrequencesCumulees[i][0]:
		i += 1
	
	if intervalle == intervalles[0]:
		p1 = (intervalle.borneInf, 0)
	else:
		p1 = (intervalle.borneInf, listeFrequencesCumulees[i - 1][1])
		
	if intervalle == intervalles[len(intervalles) - 1]:
		p2 = (intervalle.borneSup, 1)
	else:
		p2 = (intervalle.borneSup, listeFrequencesCumulees[i][1])
	
	return interpolationLineaire(p1, p2, ordre)
	
def anomaliesTukeyContinu(listeEffectifs, etendueIntervalles):
	"""Liste les valeurs aberrantes de la list, cas continu.
	
	Une valeur est dite aberrante selon la règle de Tukey si elle n'appartient pas à un intervalle I définit tel que :
	I = [Q1 - k * IQ ; Q3 + k * IQ] , k constante réelle Q1 et Q3 les quartiles, IQ l'écart inter-quartiles.
	
	La constante k est choisie arbitrairement égale à 1,5. La valeur 1.5 est selon Tukey une valeur pragmatique, qui a une raison probabiliste.
	Si une variable suit une distribution normale, alors la zone délimitée par la boîte et les moustaches devrait contenir 99,3 % des observations.
	
	:rtype: list
	:return: Collection contenant les données anormales pour la distribution des valeurs.
	"""
	listeFrequencesCumulees = calculFrequencesCumulees(calculEffectifsCumules(listeEffectifs))
	q1 = quantileContinu(0.25, listeFrequencesCumulees, etendueIntervalles)
	q3 = quantileContinu(0.75, listeFrequencesCumulees, etendueIntervalles)
	iq = q3 - q1
	interv = Intervalle(q1 - 1.5 * iq, q3 + 1.5 * iq, True, True)
	listeAnomalies = []
	for couple in listeEffectifs:
		if not interv.contient(couple[0]):
			for i in range(couple[1]):
				listeAnomalies.append(couple[0])
	#On ajoute la valeur dans resultat autant de fois qu'elle est présente dans la série.
	return listeAnomalies
	
def infoDistributionCumulativeContinue(listeEffectifsCumules, intervalles):
	"""Création d'un dictionnaire pour les informations sur la distribution cumulative des données.
	
	Couples (clé, valeur):
		* "x" : liste des abscisses, les données
		* "value" : liste des ordonnées, les effectifs cumulés respectifs
		
	:param listeEffectifCumules: liste de couples (centre de l'intervalle, effectif cumulé).
	:rtype: dict
	""" 
	abscisses = [intervalles[0].borneInf]
	values = [0]
	i = 0
	for couple in listeEffectifsCumules:
		if couple != listeEffectifsCumules[len(listeEffectifsCumules) - 1]:
			abscisses.append(intervalles[i].borneSup)
			values.append(couple[1])
		else:
			abscisses.append(intervalles[i].borneSup)
			values.append(couple[1])
		i += 1
	
	distributionC= {}
	distributionC['x'] = abscisses
	distributionC['value'] = values
	
	return distributionC
	
def infoBoiteTukeyContinu(listeEffectifs, etendueIntervalles):
	"""Création d'un dictionnaire pour la boîte à moustaches de Tukey, cas continu.
	
	Cette fonction est compatible pour les données discrètes et continues.
	
	Couples (clé, valeur):
		* "q1" : premier quartile
		* "q3" : troisième quartile
		* "median" : la médiane de la série de données
		* "left" : extrémité de la moustache gauche, Q1 - k * (Q3 - Q1)
		* "droite" : extrémité de la moustache droite, Q3 + k * (Q3 - Q1)
		* "outliers" : une liste des anomalies statistiques
	
	:param listeEffectifs: liste de couples (valeur, effectif).
	:param etendueIntervalles: partition de l'étendue de la série des données, issue de la discrétisation.
	:rtype: dict
	"""	
	listeFC = calculFrequencesCumulees(calculEffectifsCumules(listeEffectifs))
	q1 = quantileContinu(0.25, listeFC, etendueIntervalles)
	q3 = quantileContinu(0.75, listeFC, etendueIntervalles)
	median = quantileContinu(0.5, listeFC, etendueIntervalles)
	
	tukey = {}
	tukey['q1'] = q1
	tukey['q3'] = q3
	tukey['median'] = median
	tukey['left'] = q1 - 1.5 * (q3 - q1)
	tukey['right'] = q3 + 1.5 * (q3 - q1)
	tukey['outliers'] = anomaliesTukeyContinu(listeEffectifs, etendueIntervalles)
		
	return tukey
	
def infoStats(listeEffectifs, etendueIntervalles):
	"""Création d'un dictionnaire pour le résumé des informations statistiques.
	
	Couples (clé, valeur):
		* "Min" : la valeur minimale de la série
		* "Max" : la valeur maximale de la série
		* "Range" : la différence entre le ``Max`` et le ``Min``
		* "IQR" : l'écart inter-quartiles, valeur de l'étendue regroupant 75% des données
		* "Mean" : la moyenne arithmétiqued
		* "Median" : la médiane de la série de données
		* "StdDev" : l'écart-type de la série de données
		* "Outliers" : une liste des anomalies statistiques
		
	:param listeEffectifCumules: liste de couples (centre de l'intervalle, effectif cumulé).
	:param etendueIntervalles: partition de l'étendue de la série des données, issue de la discrétisation.
	:rtype: dict
	""" 
	listeFrequencesCumulees = calculFrequencesCumulees(calculEffectifsCumules(listeEffectifs))
	
	stats = {}
	stats["Min"] = listeEffectifs[0][0]
	stats["Max"] = listeEffectifs[-1][0]
	stats["Range"] = stats["Max"] - stats["Min"]
	stats["IQR"] = quantileContinu(0.75, listeFrequencesCumulees, etendueIntervalles) - quantileContinu(0.25, listeFrequencesCumulees, etendueIntervalles)
	stats["Mean"] = moyenne(listeEffectifs)
	stats["Median"] = quantileContinu(0.5, listeFrequencesCumulees, etendueIntervalles)
	stats["StdDev"] = ecartType(variance(listeEffectifs))
	stats["Outliers"] = anomaliesTukeyContinu(listeEffectifs, etendueIntervalles)
	
	return stats
