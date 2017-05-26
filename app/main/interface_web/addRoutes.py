#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Fichier ``addRoutes.py`` contenant les fonctions d'échanges ajax/serveur
	========================================================================
        

"""
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, Blueprint, jsonify,  Response, session
from werkzeug.utils import secure_filename
import os, io, json, glob


addRoute = Blueprint('addRoute', __name__, static_folder='static/', template_folder='templates')

@addRoute.route('/iStats')
def iStats():
    """
    Fonction réalisant un échange ajax entre le serveur et la page web pour envoyer les données Statistiques

    :return jsonify(data): data sérialisé en dictionnaire, où data contient les informations de 'stat.js'
    """
    stats_path = os.path.join(addRoute.static_folder, 'json/stats.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)

@addRoute.route('/timeSeries')
def timeSeries():
    """
    Fonction réalisant un échange ajax entre le serveur et la page web pour envoyer les données des séries Temporelles

    :return jsonify(data): data sérialisé en dictionnaire, où data contient les informations de 'timeSeries.js'
    """
    stats_path = os.path.join(addRoute.static_folder, 'json/timeSeries.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)

@addRoute.route('/distribution')
def distribution():
    """
     Fonction réalisant un échange ajax entre le serveur et la page web pour envoyer les données de la ditribution

    :return jsonify(data): data sérialisé en dictionnaire, où data contient les informations de 'distribution.js'
    """
    stats_path = os.path.join(addRoute.static_folder, 'json/distribution.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)

@addRoute.route('/distributionCumulative')
def distributionCumulative():
    """
    Fonction réalisant un échange ajax entre le serveur et la page web pour envoyer les données de la ditribution cumulatives

    :return jsonify(data): data sérialisé en dictionnaire, où data contient les informations de 'distributionCumulative.js'
    """
    stats_path = os.path.join(addRoute.static_folder, 'json/distributionCumulative.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)
