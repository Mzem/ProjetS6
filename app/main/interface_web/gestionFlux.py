#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Gestion des flux``
	========================================================


"""

from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import io
import json
import glob
from interface_web.choixFichier import choixFic
from chargement_des_donnees.verificationFormatFichier import *

UPLOAD_FOLDER = 'interface_web/static/uploads'
app = Flask(__name__)
app.register_blueprint(choixFic)

@app.route("/", methods=['GET'])
def index():
    """Fonction qui afficher le template "index.html" lorsque la requette HTTP "/" est indiquée.
    
    :return: retour le template "index.html"
    """
    return render_template("index.html")


@app.route("/fenetre_choix_fichier/<file>",methods=['GET','POST'])
def fenetre_choix_fichier(file):
    """Fonction qui afficher le template "choix_fichier.html" lorsque la requette HTTP "/fenetre_choix_fichier/<file>" est indiquée, et
    <file> représente le nom du fichier passé en argument de la page.
    
    :param file: représente le nom du fichier charger
    :return: retour le template "choix_fichier.html"
    """
    chemin = '{}{}'.format('interface_web/static/uploads/',file)
    fichierCSV = ouvrir(chemin) # Ouverture du fichier CSV et vérification
    if type(fichierCSV) != str : 
        verif = True
    else : 
        verif = False
    return render_template("choix_fichier.html", file=file, fichierCSV=fichierCSV, verif=verif)

@app.route("/fenetre_role_choix_colonne/<fichierCSV>",methods=['GET','POST'])
def fenetre_role_choix_colonne(fichierCSV):
    """Fonction qui afficher le template "role_choix_colonne.html" lorsque la requette HTTP "/fenetre_role_choix_colonne/" est indiquée avec comme argument
    le fichierCSV.
    
    :param fichierCSV: fichier CSV
    :type fichierCSV: TextIoWrapper
    :return: retour le template "role_choix_colonne.html"
    """
    return fichierCSV
    #return render_template("role_choix_colonne.html", fichierCSV=fichierCSV)

@app.route("/fenetre_resultat_ADD/",methods=['GET','POST'])
def fenetre_resultat_ADD():
    """Fonction qui afficher le template "resultat_ADD.html" lorsque la requette HTTP "/fenetre_resultat_ADD/" est indiquée.
    
    :return: retour le template "resultat_ADD.html"
    """
    return render_template("resultat_ADD.html")

