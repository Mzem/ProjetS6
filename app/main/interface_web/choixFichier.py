#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Fenêtre choix fichier``
	========================================================


"""
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, Blueprint
from werkzeug.utils import secure_filename
import os, sys



choixFic = Blueprint('choixFic', __name__, template_folder='templates')
UPLOAD_FOLDER = 'interface_web/static/uploads'

# Fonction pour upload fichier SGF (A voir pour renvoyer le chemin du fichier uploader)
@choixFic.route('/FileWithSGF/', methods=['GET', 'POST'])
def FileWithSGF():
    """Fonction qui se charge de l'upload d'un fichier lors du parcours dans le système de gestions de fichiers.
    
    :return: redirige la page web vers la fenetre_rôle_choix_colonne avec comme parmètre le chemin du fichier uploadé.
     """
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        save_path = "{}/{}".format(UPLOAD_FOLDER, filename)
        file.save(save_path)
        return redirect(url_for("fenetre_role_choix_colonne", file=filename))
    return "error"

# Fonction pour upload fichier avec Drag&Drop
@choixFic.route('/FileWithDragDrop/', methods=['GET', 'POST'])
def FileWithDragDrop():
    """Fonction qui se charge de l'upload d'un fichier après avoir déposé ce fichier dans la zone de Drag&Drop.

    :return: redirige la page web vers la fenetre_rôle_choix_colonne avec comme parmètre le chemin du fichier uploadé.
     """    
    if request.method == 'POST':    
        file = request.files["file2upload"]
        filename = secure_filename(file.filename)
        save_path = "{}/{}".format(UPLOAD_FOLDER, filename)
        file.save(save_path)
        return redirect(url_for("fenetre_role_choix_colonne", file=filename))
    return "error"
