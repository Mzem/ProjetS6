"""
	Le module ``Analyse de données qualitatives``
	========================================================


"""
from flask import Flask
import os
import json
import glob

# Fonction utilisé pour calculer le nombred'élements utilisé pour construire ListeEffectifs
def nbElemListeCouple(listeEffectifs):
    """Calcul l'effectif total des données de listeEffectifs.

    La fonction se charge simple de calculer l'effectif total des données contenu dans la listeEffectifs ens sommant 
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
    """Calcul l'effectifs pour chaque données contenu dans listeDonnees.

    La fonction prend en entrée une liste contenant les données à analyser. Elle calculera les effectifs pour chaque valeur à 
    l'aide d'un dictionnaire. Ce dictionnaire sera converti en liste de tuples et un tri sera effectué sur pour ordonner les
    tuples.

    :param listeDonnees: liste contenant les données à analyser
    :return: listeEffectifs: liste de tuples (donnée, effectif)
    :rtype: list
    """   
    # Création d'un dictionnaire où chaque clé correspond à une valeur de listeDonnees, 
    # et dont la veleur est initialisé à 0.
    effectifs = {}.fromkeys(set(listeDonnees),0)
    
    for valeur in listeDonnees:
        effectifs[valeur] += 1
    
    # On retoune le dictionnaire converti en liste de couple (valeur, effectif) et trié par ordre croissant de valeur.
    listeEffectifs = sorted(effectifs.items())    
    return listeEffectifs

def calculEffectifsCumules(listeEffectifs):
    """Calcul l'effectifs cumulés avec l'aide de listeEffectifs.

    La fonction prend en entrée la liste des effectifs. Elle calculera dans une nouvelle liste l'effectifs cumulés à partir 
    de "listeEffectifs" en remplaçant l'effectif par l'effectif cumulés.

    :param listeEffectifs: liste de tuples (donnée, effectif)
    :return: listeEffectifsCumules: liste de tuples (donnée, effectif cumulé)
    :rtype: list
    """   
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
    """Calcul les fréquences d'apparitions des valeurs.

    La fonction prend en entrée la liste des effectifs. Elle calculera dans une nouvelle liste la fréquence à partir 
    de "listeEffectifs" en remplaçant l'effectif par la fréquence.

    :param listeEffectifs: liste de tuples (donnée, effectif)
    :return: listeFrequences: liste de tuples (donnée, frequence)
    :rtype: list    
    """
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
    """Calcul les fréquences cumulés pour une liste de fréquences.

    La fonction prend en entrée la liste des frequences. Elle calculera dans une nouvelle liste la fréquence à partir 
    de "listeFrequence" en remplaçant la fréquence par la fréquence cumulé.

    :param listeFrequences: liste de tuples (donnée, frequence)
    :return: listeFrequences: liste de tuples (donnée, frequence cumulé)
    :rtype: list        
    """
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
    

def infoSecteurs(listeFrequences):
    """Stock dans un fichier JSON les informations nécessaire à la création d'un diagramme de secteurs.

    La fonction prend en entrée le résultat du calcul des fréquences .Elle va créer un fichier .json pour y stocker (écrire)
    les données nécessaires à la construction du diagramme en secteurs. Pour chaque couple (fréquence,valeur) elle va associer 
    un angle compris entre 0°et 360°.

    :param listeFrequences: liste de tuples (donnée, fréquence)     
    """
    # Construction du dictionnaire qui sera mis dans le .json
    secteur = {}
    secteur['bindto'] = '#pie' # Dans le template "resultatADD", l'histogramme sera placer dans la zone s'appellant #pie
    secteur['data'] = {}
    secteur['data']['colums'] = listeFrequences
    secteur['data']['type'] = 'pie'
    
    # Stockage des données pour le diagramme de secteur dans "secteur.json"
    with open('../interface_web/static/json/secteur.json', 'w', encoding='utf-8') as f:
        json.dump(secteur, f, indent=4)  

def infoHistogramme(listeEffectifs):
    """Stock dans un fichier JSON les informations nécessaire à la création d'un histogramme.

    La fonction prend en entrée le résultat du calcul des effectifs préalablement stocké dans une liste listeEffectifs. Elle 
    va créer un fichier .json pour y stocker les données nécessaires à la construction de l’histogramme.

    :param listeEffectifs: liste de tuples (donnée, effectif)     
      """
    # Construction du dictionnaire qui sera mis dans le .json
    histo = {}
    histo['bindto'] = '#bar' # Dans le template "resultatADD", l'histogramme sera placer dans la zone s'appellant #bar
    histo['data'] = {}
    histo['data']['colums'] = listeEffectifs
    histo['data']['type'] = 'bar'  
    
    # Stockage des données pour l'histogramme dans "histogramme.json"
    with open('../interface_web/static/json/histogramme.json', 'w', encoding='utf-8') as f:
        json.dump(histo, f, indent=4)    
        