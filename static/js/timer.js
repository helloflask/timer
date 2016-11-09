
// timer function
function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    var refresh = setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.text(minutes + " : " + seconds);

        if (--timer < 0) {
            display.text("Time Over!");
            clearInterval(refresh);  // exit refresh loop
            var music = $("#over_music")[0];
            music.play();
            alert("Time Over!");
        }
    }, 1000);

}

// start timer
jQuery(function ($) {
    var display = $('#time');
    startTimer(Minutes, display);
});

// center the content
$(window).resize(function(){

	$('.timer').css({
		position:'absolute',
		left: ($(window).width() - $('.timer').outerWidth())/2,
		top: ($(window).height() - $('.timer').outerHeight())/2
	});

});

// To initially run the function:
$(window).resize();
// show help information
$('#help-info').hide();
$('#help-btn').hover( function() { $('#help-info').toggle(); } );