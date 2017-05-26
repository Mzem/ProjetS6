$.getJSON("/iStats", function(json) {
	var htmlStats = "";
	var htmlOutliers = "";
	
	$.each(json, function(key, value){
		if(key === "Outliers") {
			$.each(value, function(index, outlier) {
				htmlOutliers += "<li>" + outlier + "</li>";
			});
		}
		else {
			htmlStats += "<li><u>" + key + "</u> : " + value + "</li>";
		}
	});
		
	$('#stats').after("<div id='stats2'><h1>Statistics</h1><br> <ul>" + htmlStats + "</ul></div>");
	$('#outliers').after("<div id='outliers2'><h1>Outliers</h1><br> <ul>" + htmlOutliers + "</ul></div>");
		
});
