from flask import Flask, jsonify, render_template, request
import json
import os

@app.route('/infoStats')
def infoStats():
	
	print "#########################################"
	stats_path = os.path.join(app.static_folder, 'json/stats.json')
	with open(stats_path) as json_file:    
		data = json.load(json_file)
		print(data)
    return jsonify(data)
