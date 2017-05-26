#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	``Test module intervalleTest``
	========================================================


"""
import unittest, sys

sys.path.append('../../main')
from add.intervalle import *

class test_intervalle(unittest.TestCase): 

	@classmethod
	def setUpClass(cls):
		# i1 à i4 partition de [-12, 5]
		cls.i1 = Intervalle(-12, -6.5, True, False)
		cls.i2 = Intervalle(-6.5, 0, True, False)
		cls.i3 = Intervalle(0, 1.4, True, False)
		cls.i4 = Intervalle(1.4, 5, True, True)
		cls.i5 = Intervalle(-1, 1, False, False)
        
	@classmethod
	def tearDownClass(cls):
		pass
    
	def setUp(self):
		pass 

	def tearDown(self):
		pass
	
	def test_constructeur(self):
		self.assertEqual(self.i3.supInclus, False)
		self.assertEqual(self.i4.supInclus, True)
		
		self.assertEqual(self.i2.infInclus, True)
		self.assertEqual(self.i5.infInclus, False)
		
		self.assertEqual(self.i1.borneInf, -12)
		self.assertEqual(self.i2.borneInf, -6.5)
		self.assertEqual(self.i3.borneInf, 0)
		self.assertEqual(self.i4.borneInf, 1.4)
		
		self.assertEqual(self.i1.borneSup, -6.5)
		self.assertEqual(self.i2.borneSup, 0)
		self.assertEqual(self.i3.borneSup, 1.4)
		self.assertEqual(self.i4.borneSup, 5)
		
	def test_contient(self):
		self.assertEqual(self.i1.contient(-20), False)
		self.assertEqual(self.i1.contient(-12), True)
		self.assertEqual(self.i1.contient(-8.145), True)
		self.assertEqual(self.i1.contient(-6.5), False)
		self.assertEqual(self.i1.contient(7.864), False)
		
	def test_rechercheIntervalle(self):
		partition = [self.i1, self.i2, self.i3, self.i4]
		self.assertEqual(rechercheIntervalle(partition, -14), False)
		self.assertEqual(rechercheIntervalle(partition, -8.14), self.i1)
		self.assertEqual(rechercheIntervalle(partition, -3.22222), self.i2)
		self.assertEqual(rechercheIntervalle(partition, 0), self.i3)
		self.assertEqual(rechercheIntervalle(partition, 4.9), self.i4)
		
		
if __name__ == '__main__':
    unittest.main()
