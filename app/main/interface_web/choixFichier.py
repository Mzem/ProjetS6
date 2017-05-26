#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, render_template, send_from_directory, Blueprint
from werkzeug.utils import secure_filename
import os, sys

choixFic = Blueprint('choixFic', __name__, template_folder='templates')
UPLOAD_FOLDER = 'interface_web/static/uploads'

# Fonction pour upload fichier SGF (A voir pour renvoyer le chemin du fichier uploader)
@choixFic.route('/FileWithSGF/', methods=['GET', 'POST'])
def FileWithSGF():
    """Upload d'un fichier lors du parcours dans le système de gestion des fichiers.
    
	:return: redirection de la page web vers ``fenetre_rôle_choix_colonne`` avec comme parmètre le chemin du fichier upload.
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
    """Upload d'un fichier après avoir déposé ce fichier dans la zone de Drag&Drop.

	:return: redirection de la page web vers ``fenetre_rôle_choix_colonne`` avec comme paramètre le chemin du fichier upload.
	"""    
    if request.method == 'POST':    
        file = request.files["file2upload"]
        filename = secure_filename(file.filename)
        save_path = "{}/{}".format(UPLOAD_FOLDER, filename)
        file.save(save_path)
        return redirect(url_for("fenetre_role_choix_colonne", file=filename))
    return "error"
