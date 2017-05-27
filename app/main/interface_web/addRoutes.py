#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, render_template, send_from_directory, Blueprint, jsonify,  Response, session
from werkzeug.utils import secure_filename
import os, io, json, glob

addRoute = Blueprint('addRoute', __name__, static_folder='static/', template_folder='templates')

@addRoute.route('/iStats')
def iStats():
    """Echange ajax entre le serveur et la page web pour envoyer le compte-rendu statistique.

    :return: dictionnaire convertit en objet javascript contenantt les informations de 'stats.js'
    """
    stats_path = os.path.join(addRoute.static_folder, 'json/stats.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)

@addRoute.route('/timeSeries')
def timeSeries():
    """Echange ajax entre le serveur et la page web pour envoyer les données des séries temporelles.

    :return: dictionnaire convertit en objet javascript contenantt les informations de 'timeSeries.js'
    """
    stats_path = os.path.join(addRoute.static_folder, 'json/timeSeries.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)

@addRoute.route('/distribution')
def distribution():
    """Echange ajax entre le serveur et la page web pour envoyer les données des ditributions.

    :return: dictionnaire convertit en objet javascript contenantt les informations de 'distribution.js'
    """
    stats_path = os.path.join(addRoute.static_folder, 'json/distribution.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)

@addRoute.route('/distributionCumulative')
def distributionCumulative():
    """Echange ajax entre le serveur et la page web pour envoyer les données des ditributions cumulatives.

    :return: dictionnaire convertit en objet javascript contenantt les informations de 'distributionCumulative.js'
    """
    stats_path = os.path.join(addRoute.static_folder, 'json/distributionCumulative.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)

@addRoute.route('/boxplot')
def boxplot():
    """Echange ajax entre le serveur et la page web pour envoyer les données des boîtes de Tukey.

    :return: dictionnaire convertit en objet javascript contenantt les informations de 'boxplot.js'
    """
    stats_path = os.path.join(addRoute.static_folder, 'json/boxplot.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)
