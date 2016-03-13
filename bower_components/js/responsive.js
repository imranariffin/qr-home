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
	        		var res = res.res;
	                console.log(res);
	                console.log("change url!!!!");
	                // $('#showqr').src = res[0] + res[1] + ".jpg";
	                $('#showqr').show();
	                console.log("new src:");
	                var new_src = String(res[0]) + String(res[1]) + ".jpg";
	                console.log("desired new src: ");
	                console.log(new_src);
	                $('#showqr').attr('src', "/static/img/" + String(res[0]) + String(res[1]) + ".jpg");
	                console.log($('#showqr').attr('src'));
	        },
	        error: function (err)  {
	        	console.log(err);
	        },
	        dataType: 'json'
		});
	});
});
