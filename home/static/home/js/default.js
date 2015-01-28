$(function() {
	$('#convert_form').submit(function() {
		var n = $('#submitted-image').attr('data-hash');
		console.log(n);
		$.get('/convert/'+ n, function(d) {
			//$('#main-content').html(d);
			console.log('hello world' + d);
		});
		return false;
	});
});