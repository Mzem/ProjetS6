from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from uuid import uuid4
import os
import json
import glob

UPLOAD_FOLDER = 'interface_web/static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', '.py'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

def verifExtension(filename):
    if'.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS :
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for("fenetre_choix_fichier", filename=filename))
    return "error"

# Fonction pour upload fichier avec Drag&Drop
@app.route('/FileWithDragDrop', methods=['GET', 'POST'])
def FileWithDragDrop():
    if request.method == 'POST':    
        file = request.files["file2upload"]
        filename = secure_filename(file.filename)
        save_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)
        file.save(save_path)
        return redirect(url_for("fenetre_choix_fichier", filename=filename))
    return "error"

@app.route("/fenetre_choix_fichier/<filename>",methods=['GET','POST'])
def fenetre_choix_fichier(filename):
    #Le fichier se trouve dans /uploadr/static/upload/<filename>
    return render_template("choix_fichier.html", filepath="uploadr/static/uploads/", filename=filename)

@app.route("/fenetre_role_choix_colonne/",methods=['GET','POST'])
def fenetre_role_choix_colonne():
    return "Fenetre malek"

@app.route("/fenetre_resultat_ADD/",methods=['GET','POST'])
def fenetre_resultat_ADD():
    return "Fenetre sonny"