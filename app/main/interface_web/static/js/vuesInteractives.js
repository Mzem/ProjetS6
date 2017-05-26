$.getJSON("/timeSeries", function(json) {
	
	var timeSeries = c3.generate({
		bindto: '#timeSeries',
		data: {
			x: 'x',
			type: 'spline',
			json: json
		}
	});
});

$.getJSON("/distribution", function(json) {
	
	var distribution = c3.generate({
		bindto: '#distribution',
		data: {
			x: 'x',
			type: 'spline',
			json: json
		}
	});
});

$.getJSON("/distributionCumulative", function(json) {

	var distributionCumulative = c3.generate({
		bindto: '#distributionCumulative',
		data: {
			x: 'x',
			type: 'line',
			json: json
		}
	});
});
