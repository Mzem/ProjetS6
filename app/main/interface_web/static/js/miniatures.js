$.getJSON("/timeSeries", function(json) {
	
	var timeSeriesMini = c3.generate({
		bindto: '#timeSeriesMini',
		data: {
			x: 'timestamps',
			xFormat: '%Y-%m-%d %H:%M:%S',
			type: 'spline',
			json: json
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

$.getJSON("/distributionCumulative", function(json) {

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

var bar = c3.generate({
    bindto: '#bar',
    data: {
        columns: [
            ['data1', 30, 200, 100, 400, 150, 250],
            ['data2', 130, 100, 140, 200, 150, 50]
        ],
        type: 'bar'
    },
    bar: {
        width: {
            ratio: 0.5 // this makes bar width 50% of length between ticks
        }
        // or
        //width: 100 // this makes bar width 100px
    }
});

var pie = c3.generate({
    bindto: '#pie',
    data: {
        // iris data from R
        columns: [
            ['data1', 30],
            ['data2', 120],
        ],
        type : 'pie',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    }
});
