// Create the XHR object.
function createCORSRequest(method, url) {
	var xhr = new XMLHttpRequest();
	if ("withCredentials" in xhr) {
		// XHR for Chrome/Firefox/Opera/Safari.
		xhr.open(method, url, true);
	} else if (typeof XDomainRequest != "undefined") {
		// XDomainRequest for IE.
		xhr = new XDomainRequest();
		xhr.open(method, url);
	} else {
		// CORS not supported.
		xhr = null;
	}
	return xhr;
}

// Make the actual CORS request.
function makeCorsRequest(name) {
	// All HTML5 Rocks properties support CORS.
	if(name) {
		var url = 'http://localhost:8888/rest/rs/greeting?name=' + name;
	
		var xhr = createCORSRequest('GET', url);
		if (!xhr) {
			alert('CORS not supported');
			return;
		}
	
		// Response handlers.
		xhr.onload = function() {
			var text = xhr.responseText;
			alert(text);
			document.getElementById("t1").innerHTML = text;
			//alert('Response from CORS request to ' + url);
		};
	
		xhr.onerror = function() {
			alert('Woops, there was an error making the request.');
		};
	
		xhr.send();
	}
}

function greet() {
	//alert(document.getElementById("name").value);
	makeCorsRequest(document.getElementById("name").value);
}