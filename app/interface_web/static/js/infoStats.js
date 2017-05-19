$.getJSON("/infoStats", function(json) {
	var htmlStats = "";
	var htmlOutliers = "";
	
	$.each(json, function(key, value){
		if(key === "Outliers") {
			$.each(value, function(index, outlier) {
				htmlOutliers += "<li>" + outlier + "</li>";
			});
		}
		else {
			htmlStats += "<li>" + key + ": " + value + "</li>";
		}
	});
		
	$('#stats').after("<ul>" + htmlStats + "</ul>");
	$('#outliers').after("<ul>" + htmlOutliers + "</ul>");
		
});
