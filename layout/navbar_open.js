$(document).ready(function() {
		$(document).delegate('.navbar', 'click', function(event){
			$(this).addClass('oppenned');
			event.stopPropagation();
		});
		$(document).delegate('body', 'click', function(event) {
			$('.navbar').removeClass('oppenned');
		});
		$(document).delegate('.cls', 'click', function(event){
			$('.navbar').removeClass('oppenned');
			event.stopPropagation();
		});
	});
