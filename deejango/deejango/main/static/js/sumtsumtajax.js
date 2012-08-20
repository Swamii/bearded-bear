$(document).ready(function() {
    var form = $("#contactform");
    form.submit(function(e) {
    	$("#sendbutton").attr('disabled', true);
    	$("#sendwrapper").prepend('<span>Sending message, please wait...</span>');
    	$("#ajaxwrapper").load(
    		form.attr('action') + ' #ajaxwrapper',
    		form.serializeArray(),
    		function(responseText, responseStatus) {
    			$("#sendbutton").attr('disabled', false);
    		}
    	);
    	e.preventDefault();
    })
});