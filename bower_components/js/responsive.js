$(function (){
	$('#make-qr').click(function () {
		$.ajax({
	        type: "POST",
	        url: "/make-qr",
	        data: {
	        	'name': $("#name").val(),
	        	'contact' : $("#contact").val()
	        },
	        success: function(data) {
	                console.log(data);
	        },
	        dataType: 'json'
		});
	});
});