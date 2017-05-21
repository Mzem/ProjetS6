#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Gestion des flux``
	========================================================


"""

from flask import Flask, request, redirect, session, url_for, render_template, send_from_directory, jsonify,  Response
from werkzeug.utils import secure_filename
import os, io, json, glob
from interface_web.choixFichier import choixFic
from chargement_des_donnees.verificationFormatFichier import *
from chargement_des_donnees.analyseContenuFichier import *

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
    if type(fichierCSV) != str:
        verif = True
    else:
        verif = False
    return render_template("choix_fichier.html", file=file, verif=verif)

@app.route("/fenetre_role_choix_colonne/",methods=['GET','POST'])
def fenetre_role_choix_colonne():
    """Fonction qui afficher le template "role_choix_colonne.html" lorsque la requette HTTP "/fenetre_role_choix_colonne/" est indiquée avec comme argument
    les lignes du fichier CSV <ligneCSV> et sa description <descCSV>.
    
    :param ligneCSV: contient toutes les lignes du fichier CSV
    :param descCSV: decription du fichier CSV 
    :type ligneCSV: list
    :type descCSV: list
    :return: retour le template "role_choix_colonne.html"
    """
    
    return render_template("role_choix_colonne.html")

@app.route("/fenetre_resultat_ADD/",methods=['GET','POST'])
def fenetre_resultat_ADD():
    """Fonction qui afficher le template "resultat_ADD.html" lorsque la requette HTTP "/fenetre_resultat_ADD/" est indiquée.
    
    :return: retour le template "resultat_ADD.html"
    """
    return render_template("resultat_ADD.html")

@app.route("/remove/<file>",methods=['GET','POST'])
def remove(file):
    """Fonction qui supprime le fichier uploadé
    
    :param: file de type str correspond au nom du fichier csv
    :return: redirige vers la route index
    """
    os.remove('{}{}'.format('interface_web/static/uploads/',file))
    return redirect(url_for("index"))

@app.route('/infoStats')
def infoStats():
	stats_path = os.path.join(app.static_folder, 'json/stats.js')
	with open(stats_path) as json_file:
		data = json.load(json_file)
	return jsonify(data)

@app.route('/timeSeries')
def timeSeries():
	stats_path = os.path.join(app.static_folder, 'json/timeSeries.js')
	with open(stats_path) as json_file:
		data = json.load(json_file)
	return jsonify(data)
	
@app.route('/distribution')
def distribution():
	stats_path = os.path.join(app.static_folder, 'json/distribution.js')
	with open(stats_path) as json_file:
		data = json.load(json_file)
	return jsonify(data)
	
@app.route('/distributionCumulative')
def distributionCumulative():
	stats_path = os.path.join(app.static_folder, 'json/distributionCumulative.js')
	with open(stats_path) as json_file:
		data = json.load(json_file)
	return jsonify(data)

@app.route("/sauvegardeResultats")
def sauvegardeResultats():
    csv = '1,2,3\n4,5,6\n'
    return Response(
	    csv,
	    mimetype="text/csv",
	    headers={"Content-disposition":
	             "attachment; filename=Resultats.csv"})    
