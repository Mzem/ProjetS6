var timeSeriesMini = c3.generate({
	bindto: '#timeSeriesMini',
	data: {
		x: 'x',
		type: 'spline',
        json: {
			x: [30, 50, 100, 200, 300, 450],
			value: [130, 100, 140, 200, 150, 300]
		}
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
        json: {
			x: [30, 50, 100, 400, 500, 650],
			value: [130, 100, 140, 200, 150, 50]
		}
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
        json: {
			x: [30, 50, 100, 400, 500, 650],
			value: [130, 230, 370, 570, 720, 770]
		}
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
