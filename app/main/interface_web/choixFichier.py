#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Le module ``Fenêtre choix fichier``
	========================================================


"""
from flask import Flask

app = Flask(__name__)
UPLOAD_FOLDER = 'interface_web/static/uploads'
ALLOWED_EXTENSION = set(['csv'])

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
            return redirect(url_for("fenetre_choix_fichier", filename=filename))
    return "error"

# Fonction pour upload fichier avec Drag&Drop
@app.route('/FileWithDragDrop/', methods=['GET', 'POST'])
def FileWithDragDrop():
    if request.method == 'POST':    
        file = request.files["file2upload"]
        filename = secure_filename(file.filename)
        save_path = "{}/{}".format(UPLOAD_FOLDER, filename)
        file.save(save_path)
        return redirect(url_for("fenetre_choix_fichier", filename=filename))
    return "error"
