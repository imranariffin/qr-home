$(function (){
	$('#make-qr').click(function () {
		$.ajax({
	        type: "POST",
	        url: "/make-qr",
	        data: {
	        	'name': $("#name").val(),
	        	'emergencyContact' : $("#emergencyContact").val()
	        },
	        success: function(res) {
	                console.log(res);
	                $('#showqr').show();
	        },
	        dataType: 'json'
		});
	});
});
