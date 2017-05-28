//dataTimeSeries contient deux tableaux, contenant les données des séries temporelles pour chaque couple (enfant, parent) distinct
var dataTimeSeries = {
	"timestamps": [],
	"value": [],
	"enfant": [],
	"parent": []
};

$.getJSON("/timeSeries", function(json) {
	
	//Identification des différents arcs pour les différentes timeseries
	var i = 0,
		j = 0;
	
	var tmp1 = json["enfant"][0],
		tmp2 = json["parent"][0];
	while(i < json["timestamps"].length) {
		
		if(json["enfant"][i] != tmp1 || json["parent"][i] != tmp2) {
			
			dataTimeSeries["enfant"].push(tmp1);
			dataTimeSeries["parent"].push(tmp2);
			dataTimeSeries["timestamps"].push(json["timestamps"].slice(j, i));
			dataTimeSeries["value"].push(json["value"].slice(j, i));
			
			j = i;
			tmp1 = json["enfant"][i];
			tmp2 = json["parent"][i];
		}
		
		i++;
	}
	
	dataTimeSeries["enfant"].push(tmp1);
	dataTimeSeries["parent"].push(tmp2);
	dataTimeSeries["timestamps"].push(json["timestamps"].slice(j));
	dataTimeSeries["value"].push(json["value"].slice(j));
	
	//Par défaut, le premier arc est la première série affichée
	var currentTimeSeries = {
		"timestamps": dataTimeSeries["timestamps"][0],
		"value": dataTimeSeries["value"][0]
	}
	
	//Vue principale
	var timeSeries = c3.generate({
		bindto: '#timeSeries',
		data: {
			x: 'timestamps',
			xFormat: '%Y-%m-%d %H:%M:%S',
			json: currentTimeSeries,
			type: 'spline'
		},
		axis: {
			x: {
				type: 'timeseries'
			}
		}
	});
	
	//Vue miniature
	var timeSeriesMini = c3.generate({
		bindto: '#timeSeriesMini',
		data: {
			x: 'timestamps',
			xFormat: '%Y-%m-%d %H:%M:%S',
			type: 'spline',
			json: currentTimeSeries
		},
		axis: {
			x: {
				type: 'timeseries',
				show: false
			},
			y: {
				show: false
			}
		},
		legend: {
			show: false
		},
		tooltip: {
			show:false
		},
		point: {
			show: false
		}
	});
	
	//Création des éléments pour sélectionner la série à afficher
	// <span>nom de l'arc<span/> dans <div id = "timeSeries">
	i = 0;
	var formArc = "<form>";
	while(i < dataTimeSeries["value"].length){
		//Parent->Enfant
		formArc += "<div id='Arc'><input type='radio' class='arcTimeSeries' name='Arc'><b>" + dataTimeSeries["parent"][i] + " -> " + dataTimeSeries["enfant"][i] + "</b></div>";
		//$("#time").append("<input type='radio' class='arcTimeSeries'><b>" + dataTimeSeries["parent"][i] + " -> " + dataTimeSeries["enfant"][i] + "</b><br>");
		i++;
	}
	$("#navTimeSeries").append(formArc);
	//t'as refermé le formulaire ??
	
	//Gestion des évènements (déchargement de l'ancienne série, chargement de la nouvelle)
	$("#navTimeSeries .arcTimeSeries").each( function(index) {
		$(this).click(function() {
			
			currentTimeSeries["value"] = dataTimeSeries["value"][index];
			currentTimeSeries["timestamps"] = dataTimeSeries["timestamps"][index];
			
			timeSeries.load({
				unload: ["timestamps", "value"],
				json: currentTimeSeries
			});
			timeSeriesMini.load({
				unload: ["timestamps", "value"],
				json: currentTimeSeries
			});
		});
	});
});

$.getJSON("/distribution", function(json) {
	
	//Vue principale
	var distribution = c3.generate({
		bindto: '#distribution',
		data: {
			x: 'x',
			type: 'spline',
			json: json
		}
	});
	
	//Vue miniature
	var distributionMini = c3.generate({
		bindto: '#distributionMini',
		data: {
			x: 'x',
			type: 'spline',
			json: json
		},
		axis: {
			x: {
				show: false
			},
			y: {
				show: false
			}
		},
		legend: {
			show: false
		},
		tooltip: {
			show:false
		},
		point: {
			show: false
		}
	});
});

$.getJSON("/distributionCumulative", function(json) {
	
	//Vue principale
	var distributionCumulative = c3.generate({
		bindto: '#distributionCumulative',
		data: {
			x: 'x',
			type: 'line',
			json: json
		}
	});
	
	//Vue miniature
	var distributionCumulativeMini = c3.generate({
		bindto: '#distributionCumulativeMini',
		data: {
			x: 'x',
			type: 'line',
			json: json
		},
		axis: {
			x: {
				show: false
			},
			y: {
				show: false
			}
		},
		legend: {
			show: false
		},
		tooltip: {
			show:false
		},
		point: {
			show: false
		}
	});
});
