#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Analyse de données qualitatives``
	========================================================


"""
import os
import json
import glob

def nbElemListeCouple(listeEffectifs):
    """Calcul l'effectif total des données de listeEffectifs.

    La fonction se charge simplement de calculer l'effectif total des données contenu danslisteEffectifs en sommant 
    l'effectif de chaque tuple (couple[1]).

    :param listeEffectifs: liste de tuples (donnée, effectif)
    :return: l'effectif total des données de listeEffectifs
    :rtype: int
    """    
    i = 0
    for couple in listeEffectifs:
        i += couple[1]
    return i

def calculEffectifs(listeDonnees):
    """Calcule l'effectifs pour chaque données contenu dans listeDonnees.

    La fonction prend en entrée une liste contenant les données à analyser. Elle calculera les effectifs pour chaque valeur à 
    l'aide d'un dictionnaire. Ce dictionnaire sera converti en liste de tuples et un tri sera effectué pour ordonner les
    tuples.

    :param listeDonnees: liste contenant les données à analyser
    :return: listeEffectifs: liste de tuples (donnée, effectif)
    :rtype: list
    """   
    # Création d'un dictionnaire oé chaque clé correspond é une valeur de listeDonnees, 
    # et dont la veleur est initialisé é 0.
    effectifs = {}.fromkeys(set(listeDonnees),0)
    
    for valeur in listeDonnees:
        effectifs[valeur] += 1
    
    # On retoune le dictionnaire converti en liste de couple (valeur, effectif) et trié par ordre croissant de valeur.
    listeEffectifs = sorted(effectifs.items())    
    return listeEffectifs

def calculEffectifsCumules(listeEffectifs):
    """Calcule les effectifs cumulés avec l'aide de listeEffectifs.

    La fonction prend en entrée la liste des effectifs. Elle calculera dans une nouvelle liste les effectifs cumulés à partir 
    de "listeEffectifs" en remplaçant l'effectif par l'effectif cumulé correspondant.

    :param listeEffectifs: liste de tuples (donnée, effectif)
    :return: listeEffectifsCumules: liste de tuples (donnée, effectif cumulé)
    :rtype: list
    """   
    # Variables : somme contiendra la valeur cumulée é chaque itération
    somme = 0
    listeEffectifsCumules = []
    
    i = 0
    while i <  len(listeEffectifs):
        tmp = (listeEffectifs[i][0], listeEffectifs[i][1] + somme)
        listeEffectifsCumules.append(tmp)
        somme += listeEffectifs[i][1]
        i += 1
    return listeEffectifsCumules

def calculFrequences(listeEffectifs):
    """Calcule les fréquences d'apparition des valeurs.

    La fonction prend en entrée la liste des effectifs. Elle calculera dans une nouvelle liste la fréquence à partir 
    de "listeEffectifs" en divisant l'effectif par la taille du jeu de données.

    :param listeEffectifs: liste de tuples (donnée, effectif)
    :return: listeFrequences: liste de tuples (donnée, frequence)
    :rtype: list    
    """
    nbElem = nbElemListeCouple(listeEffectifs)
    listeFrequences = []
    i = 0
    while i <  len(listeEffectifs):
        tmp = (listeEffectifs[i][0], listeEffectifs[i][1]/float(nbElem))
        listeFrequences.append(tmp)
        i += 1
        
    return listeFrequences

def calculFrequencesCumulees(listeEffectifsCumules):
    """Calcule les fréquences cumulées.

    La fonction prend en entrée la liste des effectifs cumulés. Elle calculera dans une nouvelle liste la fréquence à partir 
    de "listeEffectifsCumules" en divisant l'effectif cumulé par l'effectif total.

    :param listeFrequences: liste de tuples (donnée, frequence)
    :return: listeFrequences: liste de tuples (donnée, frequence cumulée)
    :rtype: list        
    """
    nbElem = listeEffectifsCumules[-1][1]
    listeFrequencesCumulees = []
    i = 0
    while i <  len(listeEffectifsCumules):
        tmp = (listeEffectifsCumules[i][0], listeEffectifsCumules[i][1]/float(nbElem))
        listeFrequencesCumulees.append(tmp)
        i += 1
        
    return listeFrequencesCumulees
    

def infoSecteurs(listeFrequences):
	"""Création d'un dictionnaire pour les informations d'un diagramme de secteurs.

	La fonction prend en entrée le résultat du calcul des fréquences. Elle va créer un dictionnaire pour y stocker
	les données nécessaires à la construction du diagramme en secteurs.
	
	Un dictionnaire est utilisé pour obtenir un objet sérialisable, et donc, facilement convertible en un objet javascript par exemple.
	Ainsi, l'utilisation de ces objets pour transporter les donnée peut-être multi-plateforme.
	
	:param listeFrequences: liste de tuples (donnée, fréquence)
	"""
	secteur = {}
	for couple in listeFrequences:
		secteur[couple[0]] = couple[1]	
	
	return secteur

def infoHistogramme(listeEffectifs):
	"""Création d'un dictionnaire pour les informations d'un histogramme (diagramme en batons).

	La fonction prend en entrée le résultat du calcul des effectifs préalablement stocké dans une liste ``listeEffectifs``. Elle va créer un dictionnaire pour y stocker
	les données nécessaires à la construction de l'histogramme.
	
	:Example:
	
	:param listeEffectifs: liste de tuples (donnée, effectif)     
    """
        
	abscisses = []
	values = []
	for couple in listeEffectifs:
		abscisses.append(couple[0])
		values.append(couple[1])
		
	histo = {}
	histo['x'] = abscisses
	histo['value'] = values 
	
	return histo
