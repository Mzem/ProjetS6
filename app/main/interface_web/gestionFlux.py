#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Gestion des flux``
	========================================================


"""

from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import json
import glob
from interface_web.choixFichier import choixFic

UPLOAD_FOLDER = 'interface_web/static/uploads'
ALLOWED_EXTENSION = set(['csv','py','png','jpg'])
app = Flask(__name__)
app.register_blueprint(choixFic)

@app.route("/", methods=['GET'])
def index():
    """
    Fonction qui afficher le template "index.html" lorsque la requette HTTP "/" est indiquée.
    
    return: retour le template "index.html"
    """
    return render_template("index.html")


@app.route("/fenetre_choix_fichier/<file>",methods=['GET','POST'])
def fenetre_choix_fichier(file):
    """
    Fonction qui afficher le template "choix_fichier.html" lorsque la requette HTTP "/fenetre_choix_fichier/<file>" est indiquée, et
    <file> représente le nom du fichier passé en argument de la page.
    
    param: file, représente le nom du fichier charger
    return: retour le template "choix_fichier.html"
    """
    #Le fichier se trouve dans /uploadr/static/uploads/<filename>
    return render_template("choix_fichier.html", filepath=UPLOAD_FOLDER, file=file)

@app.route("/fenetre_role_choix_colonne/",methods=['GET','POST'])
def fenetre_role_choix_colonne():
    """
    Fonction qui afficher le template "role_choix_colonne.html" lorsque la requette HTTP "/fenetre_role_choix_colonne/" est indiquée.
    
    return: retour le template "role_choix_colonne.html"
    """
    return render_template("role_choix_colonne.html")

@app.route("/fenetre_resultat_ADD/",methods=['GET','POST'])
def fenetre_resultat_ADD():
    """
    Fonction qui afficher le template "resultat_ADD.html" lorsque la requette HTTP "/fenetre_resultat_ADD/" est indiquée.
    
    return: retour le template "resultat_ADD.html"
    """
    return render_template("resultat_ADD.html")

