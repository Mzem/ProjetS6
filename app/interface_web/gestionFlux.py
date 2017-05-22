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
from chargement_des_donnees.verificationFormatFichier import ouvrir
from chargement_des_donnees.analyseContenuFichier import analyseFichier
from add.addQualitatives import *


app = Flask(__name__)
app.register_blueprint(choixFic)

@app.route("/fenetre_choix_fichier/", methods=['GET'])
def index():
    """Fonction qui affiche le template "choix_fichier.html" lorsque la requette HTTP "/fenetre_choix_fichier/" est indiquée.
    
    :return: retourne le template "choix_fichier.html"
    """
    return render_template("choix_fichier.html")


@app.route("/fenetre_role_choix_colonne/<file>",methods=['GET','POST'])
def fenetre_role_choix_colonne(file):
    """Fonction qui affiche le template "role_choix_colonne.html" lorsque la requette HTTP "/fenetre_role_choix_colonne/" est indiquée.
    
    :param file: représente le nom du fichier chargé
    :return: retourne le template "role_choix_colonne.html"
    """
    chemin = '{}{}'.format('interface_web/static/uploads/',file)
    fichierCSV =  ouvrir(chemin)
    
    if type(fichierCSV) == str:
        return render_template("role_choix_colonne.html", msgErreur=fichierCSV, file=file)
    
    lignesCSV, descCSV = analyseFichier(fichierCSV)
    return render_template("role_choix_colonne.html", lignesCSV=lignesCSV, descCSV=descCSV)


@app.route("/fenetre_resultat_ADD/",methods=['GET','POST'])
def fenetre_resultat_ADD():
    """Fonction qui affiche le template "resultat_ADD.html" lorsque la requette HTTP "/fenetre_resultat_ADD/" est indiquée.
    
    :return: retourne le template "resultat_ADD.html"
    """
    return render_template("resultat_ADD.html")

@app.route("/remove/<file>",methods=['GET','POST'])
def remove(file):
    """Fonction qui supprime le fichier uploadé
    
    :param: file de type str correspondant au nom du fichier csv
    :return: redirige vers la route index
    """
    os.remove('{}{}'.format('interface_web/static/uploads/',file))
    return redirect(url_for("index"))

@app.route("/calcul/",methods=['POST'])
def calcul():
    listeDonnees = request.files["liste"]
    # Demander à sonny les calcules à faire.
    
    return redirect(url_for("fenetre_resultat_ADD"))

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
