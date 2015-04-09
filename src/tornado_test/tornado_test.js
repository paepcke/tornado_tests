function ExportClass() {

    var keepAliveTimer = null;
    var keepAliveInterval = 15000; /* 15 sec*/
    var screenContent = "";
    var source = null;
    var ws = null;
    var chosenCourseNameObj = null;
    var timer = null;
    // Form node containing the course name
    // selection list:
    var crsNmFormObj = null; 
    var encryptionPwd = null;
    // Regex to separate course name from the enrollment column:
    var courseNameSepPattern = /([^\s,])*/;

    /*----------------------------  Constructor ---------------------*/
    this.construct = function() {

	originHost = window.location.host;
	//********
	alert("Local constructor called; originHost is " + originHost);
	//******ws = new WebSocket("wss://" + originHost + ":8080/exportClass");
	//******ws = new WebSocket("wss://" + originHost + ":8080/websocket");
	ws = new WebSocket("wss://mono.stanford.edu:9443");
	//********

	ws.onopen = function() {
	    //keepAliveTimer = window.setInterval(function() {sendKeepAlive()}, keepAliveInterval);
	    alert('Opened Websocket')
	};

	ws.onclose = function() {
	    clearInterval(keepAliveTimer);
	    alert("The browser or server closed the connection, or network trouble; please reload the page to resume.");
	}

	ws.onerror = function(evt) {
	    clearInterval(keepAliveTimer);
	    alert("The browser has detected an error while communicating withe the data server: " + evt.data);
	}

	ws.onmessage = function(evt) {
	    // Internalize the JSON
	    // e.g. "{resp : "courseList", "args" : ['course1','course2']"
	    try {
		alert("Got response from server.")
	    } catch(err) {
		alert('Error report from server (' + oneLineData + '): ' + err );
		return
	    }

	// ws.onmessage = function(evt) {
	//     // Internalize the JSON
	//     // e.g. "{resp : "courseList", "args" : ['course1','course2']"
	//     try {
	// 	var oneLineData = evt.data.replace(/(\r\n|\n|\r)/gm," ");
	// 	var argsObj = JSON.parse(oneLineData);
	// 	var response  = argsObj.resp;
	// 	var args    = argsObj.args;
	//     } catch(err) {
	// 	alert('Error report from server (' + oneLineData + '): ' + err );
	// 	return
	//     }
	//     handleResponse(response, args);
	}
    }();
}
    var classExporter = new ExportClass();
    alert("ExportClass instance was created.")
