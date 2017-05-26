#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	``Test module addQuantitativesContinuesTest``
	========================================================


"""
import unittest, sys, random

sys.path.append('../../main')

from add.addQualitatives import *
from add.addQuantitativesDiscretes import *
from add.addQuantitativesContinues import *

class test_addQuantitativesContinues(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass
    
	def setUp(self):
		pass

	def tearDown(self):
		pass
	
	def test_discretisation(self):
		donneesContinues = []
		taille = random.randrange(100)
		
		for i in range(taille):
			donneesContinues.append(random.uniform(-500000, 500000))
			
		listeIntervalles, etendueIntervalles = discretisation(calculNombreClasses(donneesContinues), donneesContinues)
				
		# Vérification 1 : il y a autant d'élément dans la première liste de retour que d'éléments générés
		self.assertEqual(len(listeIntervalles), taille)
		
		# Vérification 2 : toutes les dnnées continues générées appartiennent bien à un intervalle de l'étendue
		for i in donneesContinues:
			self.assertEqual(rechercheIntervalle(etendueIntervalles, i) != False, True)
		
		# Vérification 3 : la 2e valeur de retour est bien une partition de l'étendue
		self.assertEqual(etendueIntervalles[0].borneInf, min(donneesContinues))
		self.assertEqual(etendueIntervalles[-1].borneSup, max(donneesContinues))
		
		i = 0
		while i < len(etendueIntervalles) - 1:
			self.assertEqual(etendueIntervalles[i].borneSup, etendueIntervalles[i + 1].borneInf)
			self.assertEqual(etendueIntervalles[i].supInclus, False)
			self.assertEqual(etendueIntervalles[i].infInclus, True)
			i += 1
		
	def test_interpolationLineaire(self):
		#pour la première bissectrice, sa fonction mathématique donne l'image égal à l'abscisse
		self.assertEqual(interpolationLineaire((0, 0), (1, 1), 2),		2)
		self.assertEqual(interpolationLineaire((0, 0), (1, 1), -4),		-4)
		self.assertEqual(interpolationLineaire((0, 0), (1, 1), 0.8885),	0.8885)
		self.assertEqual(interpolationLineaire((0, 0), (1, 1), -18.93),	-18.93)
		
if __name__ == '__main__':
    unittest.main()
