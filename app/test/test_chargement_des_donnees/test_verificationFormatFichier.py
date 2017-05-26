#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	``Test module analyseContenuFichier``
	========================================================


"""
import unittest, sys, io
sys.path[:0] = ['../../main']
from chargement_des_donnees.verificationFormatFichier import *

class test_verificationFormatFichier(unittest.TestCase):
	"""Test case utilisé pour tester les fonctions du module 'verificationFormatFichier'."""
	
	def test_verifExistence(self):
		"""Test le fonctionnement de la fonction 'verifExistene'."""
		self.assertEqual(verifExistence("iDontExist.csv"),"Error: not an existing file")
		self.assertEqual(verifExistence("testOK.csv"),0)	
		
	def test_verifExtension(self):
		"""Test le fonctionnement de la fonction 'verifExtension'."""
		self.assertEqual(verifExtension("testEXT.txt"),"Error: file extension not .csv")
		self.assertEqual(verifExtension("testOK.csv"),0)		
	
	def test_verifLecture(self):
		"""Test le fonctionnement de la fonction 'verifLecture'."""
		with open("testRAW.csv", "r", encoding='utf-8') as fichierCSV:
			self.assertEqual(verifLecture(fichierCSV),"Error: not a raw text file")
		with open("testOK.csv", "r", encoding='utf-8') as fichierCSV:
			self.assertEqual(verifLecture(fichierCSV),0)	

	def test_ouvrir(self):
		"""Test le fonctionnement de la fonction 'ouvrir'."""
		self.assertEqual(ouvrir("iDontExist.csv"),"Error: not an existing file")
		self.assertEqual(ouvrir("testEXT.txt"),"Error: file extension not .csv")
		self.assertEqual(ouvrir("testRAW.csv"),"Error: not a raw text file")
		fichierCSV = ouvrir("testOK.csv")
		self.assertTrue(isinstance(fichierCSV,io.IOBase))
		fichierCSV.close()
		

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
