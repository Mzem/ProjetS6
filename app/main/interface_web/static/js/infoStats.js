$('#infoStats').click(function(){
	$.getJSON("{{ url_for('resultatsADD.infoStats') }}", function(json) {
		console.log(json);
	});
});
