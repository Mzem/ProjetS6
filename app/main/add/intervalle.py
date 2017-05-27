#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Description
	============	
	Ce module est utilisé pour une manipulation réduite des intervalles dans \ **R**\.
	
	.. code-block:: python
		
		>>> from add import intervalle
		>>> i = Intervalle(0, 1, true ,false)
		>>> i.contient(0.8)
		True
	
	L'intervalle i de l'exemple sert à représenter ``[0, 1[`` en notation mathématiques.
	
	Son utilisation dans l'application permet d'avoir des objets simples à manipuler lors de la discrétisation de données continues.
"""

class Intervalle(object):
	"""Ensemble d'objets pour représenter les intervalles de \ **R**\.
	
	Attributs:
		* borneInf ``float``: borne inférieure de l'intervalle
		* borneSup ``float``: borne supérieure de l'intervalle
		* infInclus ``boolean``: indique si la borne inférieure est comprise ou non dans l'intervalle
		* supInclus ``boolean``: indique si la borne supérieure est comprise ou non dans l'intervalle
		* centre ``float``: centre de l'intervalle
		
	"""
	
	def __init__(self, borneInf, borneSup, infInclus, supInclus):
		"""Constructeur de la classe.
		
		Initialise les attributs des paramètres données.
		
		Calcule le centre de l'intervalle et initialise l'attribut ``centre`` avec cette valeur.
		
		"""
		self.borneInf = float(borneInf)
		self.borneSup = float(borneSup)
		self.infInclus = infInclus
		self.supInclus = supInclus
		self.centre = (borneInf + borneSup) / 2
		
	def contient(self, nombre):
		"""Retourne vrai si l'argument appartient à l'intervalle, faux sinon"""
		if nombre == self.borneInf:
			return self.infInclus
		elif nombre == self.borneSup:
			return self.supInclus
		else:
			return nombre > self.borneInf and nombre < self.borneSup

def rechercheIntervalle(intervalles, nombre):
	"""Retrouve l'intervalle contenant un nombre en parmaètre
	
	Les intervalles de la liste sont distincts.
	Les intervalles de la liste forment une partition de l'étendue qu'ils représentent et sont triés.
	
	Ainsi, le nombre (on suppose qu'il appartient à l'étendue) appartient à un unique intervalle de la liste.
				
	:return: l'intervalle auquel ``nombre`` appartient, ``False`` sinon
	
	"""
	for elt in intervalles:
		if elt.contient(nombre):
			return elt
	return False 
