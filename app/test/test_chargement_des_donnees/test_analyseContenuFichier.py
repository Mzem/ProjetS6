#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	``Test module analyseContenuFichier``
	========================================================


"""
import unittest, sys
sys.path[:0] = ['../../main']
from chargement_des_donnees.analyseContenuFichier import *

class test_analyseContenuFichier(unittest.TestCase):
	"""Test case utilisé pour tester les fonctions du module 'analyseContenuFichier'."""
	def setUp(self):
		"""Initialisation des tests."""
		self.fichierCSV = ouvrir("testOK.csv")
		
	def tearDown(self):
		self.fichierCSV.close()
		
	def test_lecture(self):
		"""Lit le fichier ligne par lignes et compare chaque ligne à la ligne stockée"""
		lignesCSV = lecture(self.fichierCSV,False)
		self.fichierCSV.seek(0)	#repositionne curseur lecture fichier
		for ligne in lignesCSV:
			res = False
			ligneAttendue = self.fichierCSV.readline().replace('"','')
			ligneStockee = ",".join(ligne)
			if ligneStockee in ligneAttendue: res = True
			elif ligneAttendue.replace('\n','') in ligneStockee: res = True
			self.assertTrue(res)
		
	def test_typeDeDonnee(self):
		self.assertEqual(typeDeDonnee(''),'VIDE')
		self.assertEqual(typeDeDonnee('33'),'ENTIER')
		self.assertEqual(typeDeDonnee('3.3'),'REEL')
		self.assertEqual(typeDeDonnee('un peu de texte'),'TEXTE')
		self.assertEqual(typeDeDonnee('True'),'BOOL')
			
	def test_descriptionColonnes(self):
		lignesCSV = lecture(self.fichierCSV,False)
		descCSV = descriptionColonnes(lignesCSV)
		
		#relecture manuelle du fichier
		self.fichierCSV.seek(0)
		readerCSV = csv.reader(self.fichierCSV, delimiter=",")
		
		#Vérifications
		for i, ligne in enumerate(readerCSV):
			if i == 0:
				#Vérification des noms
				self.assertIn(",".join(descCSV["nom"]), ",".join(ligne))
				#Vérification des types attendus
				for j, nom in enumerate(ligne):
					if "time" in nom.lower() or "temps" in nom.lower() or "date" in nom.lower():
						typeAttendu = "date"
					elif "parent" in nom.lower() or "root" in nom.lower() or "racine" in nom.lower():
						typeAttendu = "parent"
					elif "enfant" in nom.lower() or "child" in nom.lower():
						typeAttendu = "enfant"
					else: typeAttendu = "nombre"
					self.assertEqual(descCSV["type"][j],typeAttendu)
			#Vérification du code d'erreur
			else:
				for j, val in enumerate(ligne):
					if j >= len(descCSV["nom"]): break
					if descCSV["type"][j] == "date" and typeDeDonnee(val) == "TEXTE":
						res = (descCSV["erreurs"][i-1][j] == "date string error") or (descCSV["erreurs"][i-1][j] == "correct")
						self.assertTrue(res)
					elif (descCSV["type"][j] == "parent" or descCSV["type"][j] == "enfant") and typeDeDonnee(val) == "ENTIER":
						self.assertEqual(descCSV["erreurs"][i-1][j],"correct")
					elif descCSV["type"][j] == "nombre" and (typeDeDonnee(val) == "REEL" or typeDeDonnee(val) == "ENTIER"):
						self.assertEqual(descCSV["erreurs"][i-1][j],"correct")
		
	#def test_analyseFichier(self): pas besoin, ne fait qu'utiliser les deux fonctions testées plus haut
		
		
# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
