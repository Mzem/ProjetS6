var timeSeriesMini = c3.generate({
	bindto: '#timeSeriesMini',
	data: {
		x: 'x',
		type: 'spline',
        url: '../../data/timeSeries.json',
        mimeType: 'json'
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

var distributionMini = c3.generate({
	bindto: '#distributionMini',
	data: {
		x: 'x',
		type: 'spline',
        url: '../../data/distribution.json',
        mimeType: 'json'
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

var distributionCumulativeMini = c3.generate({
	bindto: '#distributionCumulativeMini',
	data: {
		x: 'x',
		type: 'line',
        url: '../../data/distributionCumulative.json',
        mimeType: 'json'
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
