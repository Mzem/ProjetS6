#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Analyse de données quantitatives discrètes``
	========================================================
	
	
"""

from math import sqrt
from intervalle import Intervalle
from addQualitatives import calculEffectifsCumules, calculFrequencesCumulees
import json

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
	"""Calcule le quantile d'ordre ``ordre``.
	
	:param ordre: Nombre flottant compris entre 0 et 1.
	:param listeFrequencesCumulees: liste de couples (valeur, frequence cumulee) triée selon les valeurs 
	:return: La première valeur telle que la fréquence cumulée correspondante soit supérieure ou égale à l'ordre.
	:rtype: float
	
	.. note:: La médiane est le quantile d'ordre 1/2. Les quartiles sont les quantiles d'ordre 1/4 et 3/4.
	"""
	
	i = 0
	while listeFrequencesCumulees[i][1] < ordre:
		i += 1
		
	#A la sortie de la boucle listeFrequencesCumulees[i][1] >= ordre
	return listeFrequencesCumulees[i][0]
	
def variance(listeEffectifs):
	"""Calcule la variance."""
	
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
	"""Liste les valeurs aberrantes de la liste.
	
	Une valeur est dite aberrante selon la règle de Tukey si elle n'appartient pas à un intervalle I définit tel que :
	I = [Q1 - k * IQ ; Q3 + k * IQ] , k constante réelle Q1 et Q3 les quartiles, IQ l'écart inter-quartiles.
	
	La constante k est choisie arbitrairement égale à 1,5. La valeur 1.5 est selon Tukey une valeur pragmatique, qui a une raison probabiliste.
	Si une variable suit une distribution normale, alors la zone délimitée par la boîte et les moustaches devrait contenir 99,3 % des observations.
	
	:rtype: list
	:return: Collection contenant les données anormales pour la distribution des valeurs.
	
	"""
	
	listeFrequencesCumulees = calculFrequencesCumulees(calculEffectifsCumules(listeEffectifs))
	q1 = quantileDiscret(listeFrequencesCumulees)
	q3 = quantileDiscret(listeFrequencesCumulees)
	iq = q3 - q1
 	interv = Intervalle(q1 - 1.5 * iq, q3 + 1.5 * iq, true, true)
	
	listeAnomalies = []
	for couple in listeEffectifs:
		if not interv.contient(couple[0]):
			for i in range(couple[1]):
				listeAnomalies.append(couple[0])
	#On ajoute la valeur dans resultat autant de fois qu'elle est présente dans la série.
	return listeAnomalies

def symetrie(listeEffectifs):
	"""Calcule le coefficient de symétrie de Pearson.
	
	Si le coefficient est nul, la distribution est symétrique.
	Si le coefficient est positif, la distribution est étalée sur la droite.
	Si le coefficient est négatif, la distribution est étalée sur la gauche.
	
	
	:rtype: float
	:return: Valeur comprise entre -1 et 1.
	
	"""
	
	moy = moyenne(listeEffectifs)
	listeFrequencesCumulees = calculFrequencesCumulees(calculEffectifsCumules(listeEffectifs))
	mediane = quantileDiscret(1/2, listeFrequencesCumulees)
	ecType = ecartType(variance(listeEffectifs))
	
	return (moy - mediane) / ecType
	
def aplatissement(listeEffectifs):
	"""Calcule le coefficient d'aplatissement de Fisher.
	
	Si le coefficient est nul, la distribution suit une loi normale centrée réduite.
	Si le coefficient est inférieur à 3, la distribution est aplatie.
	Si le coefficient est supérieur à 3, les valeurs de la distribution est concentrée autour de la moyenne.
	
	:rtype: float
	
	"""
	moy = moyenne(listeEffectifs)
	
	somme, taille = 0, 0
	for couple in listeEffectifs:
		somme += ((couple[0] - moy) ** 4) * couple[1]
		taille += couple[1]
		
	momentCentreOrdre4 = somme / taille
	ecType = ecartType(variance(listeEffectifs))
	
	return  momentCentreOrdre4 / (ecType ** 4)

def infoDistributionDiscrete(listeEffectifs):
	"""Écriture dans le fichier distribution.json
	
	Format du fihier :
		Début
		{
			"x": [ liste des abscisses ],
			"value": [ liste des ordonnées / effectifs ]
		}
		Fin
		
	:param listeEffectifs: liste de couples (valeur, effectif).
	"""
	
	fichierJson = open("data/distribution.json", 'w')
	
	strX = str()
	strValues = str()
	for couple in listeEffectifs:
		if couple != listeEffectifs[len(listeEffectifs) - 1]:
			strX += str(couple[0]) + ", "
			strValues += str(couple[1]) + ", "
		else:
			strX += couple[0]
			strValues += str(couple[1])
	
	fichierJson.write("{\n\t\"x\": [" + strX + "],\n\t\"value\": [" + strValues + "]\n}")
	fichierJson.close()

def infoDistributionCumulativeDiscrete(listeEffectifsCumules):
	"""Écriture dans le fichier distributionCumulative.json
	
	Format du fihier :
		Début
		{
			"x": [ liste des abscisses ],
			"value": [ liste des ordonnées / effectifs cumulés ]
		}
		Fin
		
	:param listeEffectifCumules: liste de couples (valeur, effectif cumulé).
	"""
	
	fichierJson = open("data/distributionCumulative.json", 'w')
	
	strX = str()
	strValues = str()
	for couple in listeEffectifsCumules:
		if couple != listeEffectifsCumules[len(listeEffectifsCumules) - 1]:
			strX += str(couple[0]) + ", "
			strValues += str(couple[1]) + ", "
		else:
			strX += couple[0]
			strValues += str(couple[1])
	
	fichierJson.write("{\n\t\"x\": [" + strX + "],\n\t\"value\": [" + strValues + "]\n}")
	fichierJson.close()
	
def infoBoiteTukey(listeEffectifs):
	pass

def infoSerieTemporelle(listeSerieTemporelle):
	"""Écriture dans le fichier timeSeries.json
	
	Format du fihier :
		Début
		{
			"x": [ liste des Timestamp ],
			"value": [ liste des valeurs ]
		}
		Fin
		
	:param listeSerieTemporelle: liste de couples (Timestamp, valeur), et un Timestamp est une chaîne de caractères.
	"""
	
	fichierJson = open("data/timeSeries.json", 'w')
	
	strX = str()
	strValues = str()
	for couple in listeSerieTemporelle:
		if couple != listeSerieTemporelle[len(listeSerieTemporelle) - 1]:
			strX += couple[0] + ", "
			strValues += str(couple[1]) + ", "
		else:
			strX += couple[0]
			strValues += str(couple[1])
	
	fichierJson.write("{\n\t\"x\": [" + strX + "],\n\t\"value\": [" + strValues + "]\n}")
	fichierJson.close()
