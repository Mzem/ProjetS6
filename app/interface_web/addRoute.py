from flask import Flask, request, redirect, url_for, render_template, send_from_directory, Blueprint
from werkzeug.utils import secure_filename
import os
import io
import json


add = Blueprint('add', __name__, template_folder='templates')

@add.route('/infoStats')
def infoStats():
    stats_path = os.path.join(app.static_folder, 'json/stats.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)

@add.route('/timeSeries')
def timeSeries():
    stats_path = os.path.join(app.static_folder, 'json/timeSeries.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)

@add.route('/distribution')
def distribution():
    stats_path = os.path.join(app.static_folder, 'json/distribution.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)

@add.route('/distributionCumulative')
def distributionCumulative():
    stats_path = os.path.join(app.static_folder, 'json/distributionCumulative.js')
    with open(stats_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)