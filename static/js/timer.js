
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
    var Minutes = $("#minutes").html(),
    display = $('#time');
    startTimer(Minutes, display);
});

// progress bar
var bar = new ProgressBar.Circle(container, {
  color: '#eee',
  // This has to be the same size as the maximum width to
  // prevent clipping
  strokeWidth: 4,
  trailWidth: 2,
  easing: 'linear',
  duration: $("#duration").html(),
  text: {
    autoStyleContainer: false
  },
  from: { color: '#FFEA82', width: 2 },
  to: { color: '#4CAF50', width: 4 },
  // Set default step function for all animate calls
  step: function(state, circle) {
    circle.path.setAttribute('stroke', state.color);
    circle.path.setAttribute('stroke-width', state.width);
 var barText = $("#time").html();
      circle.setText(barText);
  }
});
bar.text.style.fontFamily = 'FranklinGothic, Verdana, Arial, sans-serif';
bar.text.style.fontSize = '80px';
bar.text.style.fontWeight = 'bold';
bar.text.style.color = '#000';

bar.animate(1.0);  // Number from 0.0 to 1.0

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