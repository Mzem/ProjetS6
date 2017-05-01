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

UPLOAD_FOLDER = 'interface_web/static/uploads'
ALLOWED_EXTENSION = set(['csv','py','png','jpg'])
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


def verifExtension(filename):
    if'.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSION :
        return 0
    else :
        return 2

# Fonction pour upload fichier SGF (A voir pour renvoyer le chemin du fichier uploader)
@app.route('/FileWithSGF/', methods=['GET', 'POST'])
def FileWithSGF():
    if request.method == 'POST':
        file = request.files['file']
        if file and verifExtension(file.filename) == 0:
            filename = secure_filename(file.filename)
            save_path = "{}/{}".format(UPLOAD_FOLDER, filename)
            file.save(save_path)
            return redirect(url_for("fenetre_choix_fichier", file=filename))
    return "error"

# Fonction pour upload fichier avec Drag&Drop
@app.route('/FileWithDragDrop/', methods=['GET', 'POST'])
def FileWithDragDrop():
    if request.method == 'POST':    
        file = request.files["file2upload"]
        filename = secure_filename(file.filename)
        save_path = "{}/{}".format(UPLOAD_FOLDER, filename)
        file.save(save_path)
        return redirect(url_for("fenetre_choix_fichier", file=filename))
    return "error"


@app.route("/fenetre_choix_fichier/<file>",methods=['GET','POST'])
def fenetre_choix_fichier(file):
    #Le fichier se trouve dans /uploadr/static/uploads/<filename>
    return render_template("choix_fichier.html", filepath=UPLOAD_FOLDER, file=file)

@app.route("/fenetre_role_choix_colonne/",methods=['GET','POST'])
def fenetre_role_choix_colonne():
    return render_template("role_choix_colonne.html")

@app.route("/fenetre_resultat_ADD/",methods=['GET','POST'])
def fenetre_resultat_ADD():
        return render_template("resultat_ADD.html")

