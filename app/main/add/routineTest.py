#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Fichier de test : à supprimer quand plus besoin
"""

from intervalle import *
from addQualitatives import *
from addQuantitativesDiscretes import *
from addQuantitativesContinues import *

def main():
	donneesContinues = [53.363,53.534,57.126,75.558,78.405,78.961,77.468,79.495,53.363,76.951,80.133,77.481,79.962,79.178,79.834,53.363,80.482,80.021,79.16,79.457,79.046,79.132,79.851,79.446,79.733,81.374,81.516,80.559,80.058,80.032,79.317,81.041]
	########### intervalle : en cours ################
	i = Intervalle(0, 1, True, False)
	#print i.contient(0)
	#print i.contient(1)
	#print i.contient(0.5)
	#print i.contient(0.99999)
	#print i.contient(-0.00001)
	#print i.contient(0.00001)
	#print i.contient(1.00001)
	intervalles = [Intervalle(0, 1, True, False),Intervalle(1, 2, True, False),Intervalle(2, 3, True, False),Intervalle(3, 4, True, True)]
	i1 = rechercheIntervalle(intervalles, 3.5)
	i2 = rechercheIntervalle(intervalles, 1)
	
	########### ADD qualitatives : OK ################
	listeEffectifs = calculEffectifs(donneesContinues)
	listeEffectifsCumules = calculEffectifsCumules(listeEffectifs)
	listeFrequences = calculFrequences(listeEffectifs)
	listeFrequencesCumulees = calculFrequencesCumulees(listeFrequences)
	
	########## ADD quantitatives discretes : OK ############
	moy = moyenne(listeEffectifs)
	quartile1 = quantileDiscret(0.25, listeFrequencesCumulees)
	mediane = quantileDiscret(0.5, listeFrequencesCumulees)
	quartile3 = quantileDiscret(0.75, listeFrequencesCumulees)
	var = variance(listeEffectifs)
	stddev = ecartType(var)
	listeAnomalies = anomaliesTukey(listeEffectifs)
	sym = symetrie(listeEffectifs)
	apl = aplatissement(listeEffectifs)
	
	########## ADD quantitatives continues : OK #########
	nombreClasses = calculNombreClasses(donneesContinues)
	listeIntervalles, etendueIntervalles = discretisation(nombreClasses, donneesContinues)
	#for intervalle in listeIntervalles:
		#print intervalle.borneInf, intervalle.borneSup
	#for intervalle in etendueIntervalles:
		#print intervalle.borneInf, intervalle.borneSup
	listeCentresIntervalles = preparationIntervallesAnalyse(listeIntervalles)
	
		#preparation pour une analyse sur des données continues => centre des intervalles
	listeEffectifs2 = calculEffectifs(listeCentresIntervalles)
	listeEffectifsCumules2 = calculEffectifsCumules(listeEffectifs2)
	listeFrequences2 = calculFrequences(listeEffectifs2)
	listeFrequencesCumulees2 = calculFrequencesCumulees(listeFrequences2)

	q1 = quantileContinu(0.25, listeFrequencesCumulees2, etendueIntervalles)
	med = quantileContinu(0.5, listeFrequencesCumulees2, etendueIntervalles)
	q3 = quantileContinu(0.75, listeFrequencesCumulees2, etendueIntervalles)
	
	
if __name__ == '__main__':
	main()
