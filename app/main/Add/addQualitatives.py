"""
	Le module ``Analyse de donn�es qualitatives``
	========================================================


"""
from flask import Flask
import os
import json
import glob


def calculEffectifs(listeDonnees):
    # Cr�ation d'un dictionnaire o� chaque cl� correspond � une valeur de listeDonnees, 
    # et dont la veleur est initialis� � 0.
    nbElem = len(listeDonnees)
    effectifs = {}.fromkeys(set(listeDonnees),0)
    
    for valeur in listeDonnees:
        effectifs[valeur] += 1
    
    # On retoune le dictionnaire converti en liste de couple (valeur, effectif) et tri� par ordre croissant de valeur.
    listeEffectifs = sorted(effectifs.items())
    listeEffectifs.append(nbElem)
    
    return listeEffectifs

def calculEffectifsCumules(listeEffectifs):
    # Variables : add contiendra la valeur cumul�e � chaque it�ration + d�finition de listeEffectifsCumules comme �tant une liste
    add = 0
    listeEffectifsCumules = []
    
    # Pour chaque couple on remplace l'effectif par l'effectif cumul�e
    i = 0
    while i <  len(listeEffectifs)-1: # Le dernier �l�ment de listeEffectifs est le nombre d'�l�ments
        tmp = (listeEffectifs[i][0], listeEffectifs[i][1] + add)
        listeEffectifsCumules.append(tmp)
        add += listeEffectifs[i][1]    # Mise � jour de add
        i += 1
    return listeEffectifsCumules

def calculFrequences(listeEffectifs):
    # On r�cup�re le nombre d'�lements qu'on analyse (situ� � la fin de la liste) 
    # + d�finition de listeFrequencesCumules comme �tant une liste
    nbElem = listeEffectifs[-1]
    listeFrequences = []
    i = 0
    while i <  len(listeEffectifs)-1: # Le dernier �l�ment de listeEffectifs est le nombre d'�l�ments
        tmp = (listeEffectifs[i][0], listeEffectifs[i][1]/nbElem)
        listeFrequences.append(tmp)
        i += 1
    listeFrequences.append(nbElem)       
    
    return listeFrequences

def calculFrequencesCumulees(listeFrequences):
    # On r�cup�re le nombre d'�lements qu'on analyse + d�finition de listeFrequencesCumules comme �tant une liste
    nbElem = listeFrequences[-1]
    add = 0
    listeFrequencesCumules = []
    
    i = 0
    while i <  len(listeFrequences)-1:
        tmp = (listeFrequences[i][0],listeFrequences[i][1]+add)
        add += listeFrequences[i][1]
        listeFrequencesCumules.append(tmp)
        i += 1
    return listeFrequencesCumules
    

def infoSecteurs(listeFrequence):
    return "vide"

def infoHistogramme(listeEffectifs):
    return "vide"