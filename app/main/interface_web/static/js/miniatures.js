$.getJSON("/timeSeries", function(json) {
	
	var timeSeriesMini = c3.generate({
		bindto: '#timeSeriesMini',
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

$.getJSON("/distribution", function(json) {
	
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

$.getJSON("/distribution", function(json) {

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
