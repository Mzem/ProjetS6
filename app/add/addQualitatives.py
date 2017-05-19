#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Analyse de donn�es qualitatives``
	========================================================


"""
from flask import Flask
import os
import json
import glob

# Fonction utilis� pour calculer le nombred'�lements utilis� pour construire ListeEffectifs
def nbElemListeCouple(listeEffectifs):
    """Calcul l'effectif total des donn�es de listeEffectifs.

    La fonction se charge simple de calculer l'effectif total des donn�es contenu dans la listeEffectifs ens sommant 
    l'effectif de chaque tuple (couple[1]).

    :param listeEffectifs: liste de tuples (donn�e, effectif)
    :return: l'effectif total des donn�es de listeEffectifs
    :rtype: int
    """    
    i = 0
    for couple in listeEffectifs:
        i += couple[1]
    return i    

def calculEffectifs(listeDonnees):
    """Calcul l'effectifs pour chaque donn�es contenu dans listeDonnees.

    La fonction prend en entr�e une liste contenant les donn�es � analyser. Elle calculera les effectifs pour chaque valeur � 
    l'aide d'un dictionnaire. Ce dictionnaire sera converti en liste de tuples et un tri sera effectu� sur pour ordonner les
    tuples.

    :param listeDonnees: liste contenant les donn�es � analyser
    :return: listeEffectifs: liste de tuples (donn�e, effectif)
    :rtype: list
    """   
    # Cr�ation d'un dictionnaire o� chaque cl� correspond � une valeur de listeDonnees, 
    # et dont la veleur est initialis� � 0.
    effectifs = {}.fromkeys(set(listeDonnees),0)
    
    for valeur in listeDonnees:
        effectifs[valeur] += 1
    
    # On retoune le dictionnaire converti en liste de couple (valeur, effectif) et tri� par ordre croissant de valeur.
    listeEffectifs = sorted(effectifs.items())    
    return listeEffectifs

def calculEffectifsCumules(listeEffectifs):
    """Calcul l'effectifs cumul�s avec l'aide de listeEffectifs.

    La fonction prend en entr�e la liste des effectifs. Elle calculera dans une nouvelle liste l'effectifs cumul�s � partir 
    de "listeEffectifs" en rempla�ant l'effectif par l'effectif cumul�s.

    :param listeEffectifs: liste de tuples (donn�e, effectif)
    :return: listeEffectifsCumules: liste de tuples (donn�e, effectif cumul�)
    :rtype: list
    """   
    # Variables : add contiendra la valeur cumul�e � chaque it�ration + d�finition de listeEffectifsCumules comme �tant une liste
    add = 0
    listeEffectifsCumules = []
    
    # Pour chaque couple on remplace l'effectif par l'effectif cumul�e
    i = 0
    while i <  len(listeEffectifs): # Le dernier �l�ment de listeEffectifs est le nombre d'�l�ments
        tmp = (listeEffectifs[i][0], listeEffectifs[i][1] + add)
        listeEffectifsCumules.append(tmp)
        add += listeEffectifs[i][1]    # Mise � jour de add
        i += 1
    return listeEffectifsCumules

def calculFrequences(listeEffectifs):
    """Calcul les fr�quences d'apparitions des valeurs.

    La fonction prend en entr�e la liste des effectifs. Elle calculera dans une nouvelle liste la fr�quence � partir 
    de "listeEffectifs" en rempla�ant l'effectif par la fr�quence.

    :param listeEffectifs: liste de tuples (donn�e, effectif)
    :return: listeFrequences: liste de tuples (donn�e, frequence)
    :rtype: list    
    """
    # On r�cup�re le nombre d'�lements qu'on analyse (situ� � la fin de la liste) 
    # + d�finition de listeFrequencesCumules comme �tant une liste
    nbElem = nbElemListeCouple(listeEffectifs)
    listeFrequences = []
    i = 0
    while i <  len(listeEffectifs): # Le dernier �l�ment de listeEffectifs est le nombre d'�l�ments
        tmp = (listeEffectifs[i][0], listeEffectifs[i][1]/float(nbElem))
        listeFrequences.append(tmp)
        i += 1
        
    return listeFrequences

def calculFrequencesCumulees(listeFrequences):
    """Calcul les fr�quences cumul�s pour une liste de fr�quences.

    La fonction prend en entr�e la liste des frequences. Elle calculera dans une nouvelle liste la fr�quence � partir 
    de "listeFrequence" en rempla�ant la fr�quence par la fr�quence cumul�.

    :param listeFrequences: liste de tuples (donn�e, frequence)
    :return: listeFrequences: liste de tuples (donn�e, frequence cumul�)
    :rtype: list        
    """
    # On r�cup�re le nombre d'�lements qu'on analyse + d�finition de listeFrequencesCumules comme �tant une liste
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
    """Stock dans un fichier JSON les informations n�cessaire � la cr�ation d'un diagramme de secteurs.

    La fonction prend en entr�e le r�sultat du calcul des fr�quences .Elle va cr�er un fichier .json pour y stocker (�crire)
    les donn�es n�cessaires � la construction du diagramme en secteurs. Pour chaque couple (fr�quence,valeur) elle va associer 
    un angle compris entre 0�et 360�.

    :param listeFrequences: liste de tuples (donn�e, fr�quence)     
    """
    # Construction du dictionnaire qui sera mis dans le .json
    secteur = {}
    secteur['bindto'] = '#pie' # Dans le template "resultatADD", l'histogramme sera placer dans la zone s'appellant #pie
    secteur['data'] = {}
    secteur['data']['columns'] = listeFrequences
    secteur['data']['type'] = 'pie'
    
    # Stockage des donn�es pour le diagramme de secteur dans "secteur.json"
    with open('../interface_web/static/json/secteur.json', 'w', encoding='utf-8') as f:
        json.dump(secteur, f, indent=4)  

def infoHistogramme(listeEffectifs):
    """Stock dans un fichier JSON les informations n�cessaire � la cr�ation d'un histogramme.

    La fonction prend en entr�e le r�sultat du calcul des effectifs pr�alablement stock� dans une liste listeEffectifs. Elle 
    va cr�er un fichier .json pour y stocker les donn�es n�cessaires � la construction de l�histogramme.

    :param listeEffectifs: liste de tuples (donn�e, effectif)     
      """
    # Construction du dictionnaire qui sera mis dans le .json
    histo = {}
    histo['bindto'] = '#bar' # Dans le template "resultatADD", l'histogramme sera placer dans la zone s'appellant #bar
    histo['data'] = {}
    histo['data']['columns'] = listeEffectifs
    histo['data']['type'] = 'bar'  
    
    # Stockage des donn�es pour l'histogramme dans "histogramme.json"
    with open('../interface_web/static/json/histogramme.json', 'w', encoding='utf-8') as f:
        json.dump(histo, f, indent=4)    
        

histo = [("Data1",5),("Data2",23),("Data3",17),("Data4",25),("Data5",1),("Data6",2)]
sect = [("Data1",0.05),("Data2",0.23),("Data3",0.17),("Data4",0.25),("Data5",0.1),("Data6",0.2)]

infoHistogramme(histo)
infoSecteurs(sect)
val = os.path.isfile('../interface_web/static/json/histogramme.json')
print("val : %s" %val)