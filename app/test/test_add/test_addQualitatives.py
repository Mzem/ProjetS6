#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	``Test module addQualitatives``
	========================================================


"""
import unittest 
import sys
sys.path[:0] = ['../../main']
from add.addQualitatives import *


class test_addQualitatives(unittest.TestCase): 

    # initialization logic for the test suite declared in the test module
    # code that is executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        pass 

    # clean up logic for the test suite declared in the test module
    # code that is executed after all tests in one test run
    @classmethod
    def tearDownClass(cls):
        pass 

    # initialization logic
    # code exécuté avant chaque test
    def setUp(self):
        pass 

    # clean up logic
    # code exécuté après chaque test
    def tearDown(self):
        pass 

    # test fonctions du module Add_qualitatives 
    def test_nbElemListeCouple(self):
        lst = [("data1",2),("data2",5),("data3",11),("data4",3)]
        nb = nbElemListeCouple(lst)
        self.assertEqual(nb,21)
    
    def test_calculEffectifs(self):
        liste = ["a","b","d","a","f","c","g","d","b","a","d","f","g","d","f","c","a","d","c","c"] # Une liste de valeurs
        listeEffectifs = calculEffectifs(liste)                 # Application de la fonction "calculEffectifs"
        res = [("a",4),("b",2),("c",4),("d",5),("f",3),("g",2)] # resultat attentu
        self.assertEqual(listeEffectifs, res)                  # Vérification du résultat 
        
    def test_calculEffectifsCumules(self):
        liste = [("a",4),("b",2),("c",4),("d",5),("f",3),("g",2)]   # Une liste d'effectifs
        listeEffectifsCumules = calculEffectifsCumules(liste)       # Application de la fonction "calculEffectifsCumules"
        res = [("a",4),("b",6),("c",10),("d",15),("f",18),("g",20)] # résultat attendu
        self.assertEqual(listeEffectifsCumules, res)               # Vérification du résultat 
        
    def test_calculFrequences(self):
        liste = [("a",4),("b",2),("c",4),("d",5),("f",3),("g",2)]   # Une liste d'effectifs
        listeFrequence = calculFrequences(liste)                    # Application de la fonction "calculFrequences"
        res = [("a",0.2),("b",0.1),("c",0.2),("d",0.25),("f",0.15),("g",0.1)] # résultat attendu
        self.assertEqual(listeFrequence, res)  # Vérification du résultat
        
    def calculFrequencesCumules(self):
        liste = [("a",0.2),("b",0.1),("c",0.2),("d",0.25),("f",0.15),("g",0.1)] # Une liste de fréquences
        listeFrequenceCumules = calculFrequences(liste)                         # Application de la fonction "calculFrequencesCumules"
        res = [("a",0.2),("b",0.3),("c",0.5),("d",0.75),("f",0.9),("g",1)]      # résultat attendu
        self.assertEqual(listeFrequenceCumules, res)  # Vérification du résultat 
        

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
