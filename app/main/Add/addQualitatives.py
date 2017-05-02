"""
	Le module ``Analyse de données qualitatives``
	========================================================


"""
from flask import Flask
import os
import json
import glob

# Fonction utilisé pour calculer le nombred'élements utilisé pour construire ListeEffectifs
def nbElemListeCouple(liste):
    i = 0
    for couple in liste:
        i += couple[1]
    return i    

def calculEffectifs(listeDonnees):
    # Création d'un dictionnaire où chaque clé correspond à une valeur de listeDonnees, 
    # et dont la veleur est initialisé à 0.
    effectifs = {}.fromkeys(set(listeDonnees),0)
    
    for valeur in listeDonnees:
        effectifs[valeur] += 1
    
    # On retoune le dictionnaire converti en liste de couple (valeur, effectif) et trié par ordre croissant de valeur.
    listeEffectifs = sorted(effectifs.items())    
    return listeEffectifs

def calculEffectifsCumules(listeEffectifs):
    # Variables : add contiendra la valeur cumulée à chaque itération + définition de listeEffectifsCumules comme étant une liste
    add = 0
    listeEffectifsCumules = []
    
    # Pour chaque couple on remplace l'effectif par l'effectif cumulée
    i = 0
    while i <  len(listeEffectifs): # Le dernier élément de listeEffectifs est le nombre d'éléments
        tmp = (listeEffectifs[i][0], listeEffectifs[i][1] + add)
        listeEffectifsCumules.append(tmp)
        add += listeEffectifs[i][1]    # Mise à jour de add
        i += 1
    return listeEffectifsCumules

def calculFrequences(listeEffectifs):
    # On récupère le nombre d'élements qu'on analyse (situé à la fin de la liste) 
    # + définition de listeFrequencesCumules comme étant une liste
    nbElem = nbElemListeCouple(listeEffectifs)
    listeFrequences = []
    i = 0
    while i <  len(listeEffectifs): # Le dernier élément de listeEffectifs est le nombre d'éléments
        tmp = (listeEffectifs[i][0], listeEffectifs[i][1]/nbElem)
        listeFrequences.append(tmp)
        i += 1
        
    return listeFrequences

def calculFrequencesCumulees(listeFrequences):
    # On récupère le nombre d'élements qu'on analyse + définition de listeFrequencesCumules comme étant une liste
    add = 0
    listeFrequencesCumules = []
    
    i = 0
    while i <  len(listeFrequences):
        tmp = (listeFrequences[i][0],listeFrequences[i][1]+add)
        add += listeFrequences[i][1]
        listeFrequencesCumules.append(tmp)
        i += 1
    return listeFrequencesCumules
    

def infoSecteurs(listeFrequence):
    return "vide"

def infoHistogramme(listeEffectifs):
    return "vide"
