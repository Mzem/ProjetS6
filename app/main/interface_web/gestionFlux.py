#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, session, url_for, render_template, send_from_directory, jsonify, send_file
from werkzeug.utils import secure_filename
import os, io, json, glob

from demoAPI import ecrireResultats, safe_open_w
from interface_web.choixFichier import choixFic
from interface_web.addRoutes import addRoute
from chargement_des_donnees.verificationFormatFichier import ouvrir
from chargement_des_donnees.analyseContenuFichier import analyseFichier
from add.addQualitatives import *
from add.addQuantitativesContinues import *
from add.addQuantitativesDiscretes import *

app = Flask(__name__)
app.register_blueprint(choixFic)
app.register_blueprint(addRoute)

def removeFiles():
    """Vide le dossier ``uploads``  et ``downloads`` contenant les fichiers chargé."""
    files = os.listdir('interface_web/static/uploads/')
    for i in range(0,len(files)):
        if files[i] != '.dummy':
            os.remove('interface_web/static/uploads/'+files[i])

    files = os.listdir('interface_web/static/downloads/')
    for i in range(0,len(files)):
        if files[i] != '.dummy':
            os.remove('interface_web/static/downloads/'+files[i])


@app.route("/", methods=['GET'])
def fenetre_choix_fichier():
    """
    Affiche le template "choix_fichier.html" lorsque la requette HTTP "/" est indiquée.
    
    Vide le dossier 'uploads/' avec la fonction ``removeFiles``
    
    :return: le rendu du template ``choix_fichier.html``
    """
    removeFiles()
    return render_template("choix_fichier.html")

@app.route("/manuel/", methods=['GET'])
def manuel():
    """
    Affiche le template manuel.html" lorsque la requette HTTP "/manuel/" est indiquée.
    
    Ce template contiend le pdf du manuel utilisateur.

    :return: le rendu du template ``manuel.html``
    """
    return render_template("manuel.html")


@app.route("/fenetre_role_choix_colonne/<file>",methods=['GET','POST'])
def fenetre_role_choix_colonne(file):
    """
    Affiche le template "role_choix_colonne.html" lorsque la requette HTTP "/fenetre_role_choix_colonne/" est indiquée.
    
    Le template affiche un message d'erreur si le fichier ``file`` n'est pas valide, sinon elle affiche son contenu.
    
    :param file: représente le nom du fichier chargé.
    :type file: str
    :return: le rendu du template ``role_choix_colonne.html``
    """
    chemin = '{}{}'.format('interface_web/static/uploads/',file)
    fichierCSV =  ouvrir(chemin)
    
    if type(fichierCSV) == str:
        return render_template("role_choix_colonne.html", msgErreur=fichierCSV, file=file)
    
    lignesCSV, descCSV = analyseFichier(fichierCSV)
    return render_template("role_choix_colonne.html", lignesCSV=lignesCSV, descCSV=descCSV, file=file)


@app.route("/fenetre_resultat_ADD/<file>",methods=['GET', 'PUT'])
def fenetre_resultat_ADD(file):
	"""
	Affiche le template "resultat_ADD.html" lorsque la requette HTTP "/fenetre_resultat_ADD/" est indiquée.
	
	Avant d'envoyer la page web, les analyses descriptives sur les colonnes sont effectuées pour renseigner les données ``json`` nécessaires.
	
	:return: le rendu du template ``resultat_ADD.html``
	"""
	if request.method == 'PUT':
		
		requette = request.get_json()
		
		colonneADD = requette['colonneADD']
		donneesIntervalles, etendueIntervalles = discretisation(calculNombreClasses(colonneADD), colonneADD)
		donneesContinues = preparationIntervallesAnalyse(donneesIntervalles)
		listeEffectifs = calculEffectifs(donneesContinues)
		listeEffectifsCumules = calculEffectifsCumules(listeEffectifs)
		
		# infos stats
		dataSummary = infoStats(listeEffectifs, etendueIntervalles)
		dataSummary["nomColonne"] = requette["nomColonne"]
		with safe_open_w('interface_web/static/json/stats.js') as f:
			json.dump(dataSummary, f, indent=4)

		# Séries temporelles
		dataTimeSeries = {}
		dataTimeSeries["timestamps"] = requette["dateADD"]
		dataTimeSeries["enfant"] = requette["enfantADD"]
		dataTimeSeries["parent"] = requette["parentADD"]
		dataTimeSeries["value"] = colonneADD
		with safe_open_w('interface_web/static/json/timeSeries.js') as f:
			json.dump(dataTimeSeries, f, indent=4)
		
		# Distribution cumulative continue
		dataDistribCumul = infoDistributionCumulativeContinue(listeEffectifsCumules, etendueIntervalles)
		with safe_open_w('interface_web/static/json/distributionCumulative.js') as f:
			json.dump(dataDistribCumul, f, indent=4)
			
		# Distribution
		dataDistrib = infoDistribution(listeEffectifs)
		with safe_open_w('interface_web/static/json/distribution.js') as f:
			json.dump(dataDistrib, f, indent=4)
			
		# Boîte à moustaches de Tukey : à décommenter si utilisé
		#dataTukey = infoBoiteTukeyContinu(listeEffectifs, etendueIntervalles)
		#with safe_open_w('interface_web/static/json/boxplot.js') as f:
		#	json.dump(dataTukey, f, indent=4)
		
		return render_template("resultat_ADD.html", file=file, nomColonne=requette["nomColonne"])
	else:	
		return render_template("resultat_ADD.html", file=file)

@app.route("/remove/<file>",methods=['GET','POST'])
def remove(file):
    """Supprime le fichier ``file`` du dossier ``uploads``.
    
	:param file: nom du fichier ``.csv``
	:type file: str
	:return: redirige vers la route ``index``
    """
    os.remove('{}{}'.format('interface_web/static/uploads/',file))
    return redirect(url_for("fenetre_choix_fichier"))

@app.route("/sauvegardeResultats/<file>")
def sauvegardeResultats(file):
    """Sauvegarde les résultats de l'analyse descriptives dans un fichier ``.csv`` et lance son téléchargement.

    :return: téléchargement du fichier ``Resultats.csv``.
    """
    ecrireResultats("interface_web/static/uploads/" + file, "interface_web/static/downloads/" + file)
    return send_file('static/downloads/' + file,
                     mimetype='text/csv',
                     attachment_filename='results_' + file,
                     as_attachment=True)    
