$(function() {
	$("#id_password").attr('value', '');
	$("#id_birthday").datepicker({
		changeMonth: true,
		changeYear: true,
		yearRange: "1900:2012"
	});
});