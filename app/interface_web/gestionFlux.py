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
    """
    Fonction qui se charge simplement de vider le dossier contenant les fichiers chargé.

    """
    files = os.listdir('interface_web/static/uploads/')
    for i in range(0,len(files)):
        if files[i] != '.dummy':
            os.remove('interface_web/static/uploads/'+files[i])

@app.route("/", methods=['GET'])
def fenetre_choix_fichier():
    """Fonction qui affiche le template "choix_fichier.html" lorsque la requette HTTP "/" est indiquée. Elle se charge également de vider le 
    dossier 'uploads/' avec la fonction removeFiles()
    
    :return: retourne le template "choix_fichier.html"
    """
    
    removeFiles()
    return render_template("choix_fichier.html")

@app.route("/manuel/", methods=['GET'])
def manuel():
    """Fonction qui affiche le template manuel.html" lorsque la requette HTTP "/manuel/" est indiquée. 
    Ce template contiend le pdf du manuel utilisateur.

    :return: retourne le template "manuel.html"
    """
    return render_template("manuel.html")


@app.route("/fenetre_role_choix_colonne/<file>",methods=['GET','POST'])
def fenetre_role_choix_colonne(file):
    """Fonction qui affiche le template "role_choix_colonne.html" lorsque la requette HTTP "/fenetre_role_choix_colonne/" est indiquée.
    Le template affiche un message d'erreur si le fichier 'file' n'est pas valide, sinon elle affiche son contenu.
    
    :param file: représente le nom du fichier chargé
    :return: retourne le template "role_choix_colonne.html"
    """
    chemin = '{}{}'.format('interface_web/static/uploads/',file)
    fichierCSV =  ouvrir(chemin)
    
    if type(fichierCSV) == str:
        return render_template("role_choix_colonne.html", msgErreur=fichierCSV, file=file)
    
    lignesCSV, descCSV = analyseFichier(fichierCSV)
    return render_template("role_choix_colonne.html", lignesCSV=lignesCSV, descCSV=descCSV, file=file)


@app.route("/fenetre_resultat_ADD/<file>",methods=['GET','POST', 'PUT'])
def fenetre_resultat_ADD(file):
	"""Fonction qui affiche le template "resultat_ADD.html" lorsque la requette HTTP "/fenetre_resultat_ADD/" est indiquée.
        Cette fonction se charge également défectuer tout les calculs autour de l'analyse descriptives de données avant l'affichage de la page.
	
	:return: retourne le template "resultat_ADD.html"
	"""
	if request.method == 'PUT':
		requette = request.get_json()
		nomColonne = requette['nomColonne']
		colonneADD = requette['colonneADD']
		dateADD = requette['dateADD']

		donneesIntervalles, etendueIntervalles = discretisation(calculNombreClasses(colonneADD), colonneADD)
		donneesContinues = preparationIntervallesAnalyse(donneesIntervalles)
        
		listeEffectifs = calculEffectifs(donneesContinues)
		listeEffectifsCumules = calculEffectifsCumules(listeEffectifs)

        # infos stats
        #infoStats(listeEffectifs) 
        # Série temporelle
        #
        
        # Distribution cumulative continue
		dataDistribCumul = infoDistributionCumulativeContinue(listeEffectifsCumules, etendueIntervalles)
		with open('interface_web/static/json/distributionCumulative.js', 'w', encoding='utf-8') as f:
			json.dump(dataDistribCumul, f, indent=4)
			
        # Distribution
		dataDistrib = infoDistributionDiscrete(listeEffectifs)
        
		with open('interface_web/static/json/distribution.js', 'w', encoding='utf-8') as f:
			json.dump(dataDistrib, f, indent=4)
            
		return render_template("resultat_ADD.html", file=file)
	else:
		return render_template("resultat_ADD.html", file=file)

@app.route("/remove/<file>",methods=['GET','POST'])
def remove(file):
    """Fonction qui supprime le fichier 'file' mis en paramètre qui se situe dans le dossier 'uploads/'.
    
    :param: file de type str correspondant au nom du fichier csv
    :return: redirige vers la route index
    """
    os.remove('{}{}'.format('interface_web/static/uploads/',file))
    return redirect(url_for("fenetre_choix_fichier"))

@app.route("/sauvegardeResultats")
def sauvegardeResultats():
    """Fonction qui sauvegarde les résultats de l'analyse descriptives dans un fichier .csv, et lance ainsi son téléchargement.

    :return: téléchargement du fichier 'Resultats.csv'.
    """
    csv = '1,2,3\n4,5,6\n'
    return Response(
	    csv,
	    mimetype="text/csv",
	    headers={"Content-disposition":
	             "attachment; filename=Resultats.csv"})    
