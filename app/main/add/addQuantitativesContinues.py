#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Analyse de données quantitatives continues``
	========================================================
	
	
"""

from math import log2
from intervalle import Intervalle, rechercheIntervalle
from addQuantitativesDiscretes import quantileDiscret
import json

def discretisation(nombreClasses, donneesContinues):
	"""Discrétise des données continues du paramètre.
	
	La fonction se charge de décomposer l’étendue [min ; max] de l’ensemble de données en ``nombreClasses`` intervalles de même étendue.
	Ensuite de remplacer les occurrences des données par l’intervalle auquel la donnée appartient.
	
	:param donneesContinues: liste de nombres flottants
	:return: liste d'intervalles, et étendue discrétisée
	
	"""
	
	nombreClasses = calculNombreClasses(donneesContinues)
	
	etendue = max(donneesContinues) - min(donneesContinues)
	tailleIntervalle = etendue / nombreClasses
	
	intervalles = []
	for i in range(nombreClasses - 1):
		tmp = Intervalle(i * tailleIntervalle, (i + 1) * tailleIntervalle, True, False)
		intervalles.append(tmp)
	
	#dernier intervalle fermé
	tmp = Intervalle((nombreClasses - 1) * tailleIntervalle, etendue, True, True)
	intervalles.append(tmp)
	
	#remplacement dans donneesContinues la donnee par l'intervalle auquel il appartient
	for i in range(len(donneesContinues)):
		donneesContinues[i] = rechercheIntervalle(intervalles, donneesContinues[i])
		
	return donneesContinues, intervalles
	
def calculNombreClasses(donneesContinues):
	"""Calcule le nombre de classes nécessaire à une discrétisation selon la règle de Sturges.
	
	:rtype: int
	
	.. warning:: Si la distribution n'est pas symétrique, le nombre de classes ne sera pas optimal.
	
	"""
	
	return 1 + log2(len(donneesContinues))
	
def preparationIntervallesAnalyse(listeIntervalles):
	"""Prépare les données pour l’utilisation des éléments de calcul du module ADD quantitatives discrètes.
	
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
	
def infoDistributionCumulativeContinue(listeEffectifsCumulees, intervalles):
	"""Écriture dans le fichier distributionCumulative.json
	
	Format du fihier :
		Début
		{
			"x": [ liste des abscisses / bornes des intervalles ],
			"value": [ liste des ordonnées / effectifs cumulés ]
		}
		Fin
		
	:param listeEffectifCumules: liste de couples (centre de l'intervalle, effectif cumulé).
	"""
	
	fichierJson = open("data/distributionCumulative.json", 'w')

	strX = str(intervalles[0].borneInf) + ", "
	strValues = "0, "
	i = 0
	for couple in listeEffectifsCumules:
		if couple != listeEffectifsCumules[len(listeEffectifsCumules) - 1]:
			strX += str(intervalles[i].borneSup) + ", "
			strValues += str(couple[1]) + ", "
		else:
			strX += str(intervalles[i].borneSup)
			strValues += str(couple[1])
		i += 1
	
	fichierJson.write("{\n\t\"x\": [" + strX + "],\n\t\"value\": [" + strValues + "]\n}")
	fichierJson.close()
