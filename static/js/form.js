$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				command : $('#command').val(),
			},
			type : 'POST',
			url : '/solution'
		})
		.done(function(data) {
		   // $('#successAlert').text(data.name).show();
            if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}


				});

		event.preventDefault();

	});

});