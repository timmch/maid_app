$(document).ready(function() {
	$('#alertBox').delay(5000).slideUp('slow');
});

$('.apptPop').mouseover().popover('show');
$('.apptPop').mouseleave().popover('hide');

$(document).ready(function() {
	$('.dropdown-toggle').dropdown();
});

$(function() {
	$( "#from" ).datepicker({
		defaultDate: "+1w",
		changeMonth: true,
		numberOfMonths: 3,
		onSelect: function( selectedDate ) {
			$( "#to" ).datepicker( "option", "minDate", selectedDate );
		}
	});
	$( "#to" ).datepicker({
		defaultDate: "+1w",
		changeMonth: true,
		numberOfMonths: 3,
		onSelect: function( selectedDate ) {
			$( "#from" ).datepicker( "option", "maxDate", selectedDate );
		}
	});
});

$("#dropper").click(function(){
	$("#drop").slideToggle();
	$("#dropper").html("<i class='icon-chevron-up icon-white' id='iconSwitch'></i> Finish Now");
});


// Handles the sidebar collapsibles

$(document).ready(function() {
	$('#comments > .sideInfo').hide();
	$('#timeoff > .sideInfo').hide();
	$('#unconfirmed > .sideInfo').hide();
	$('#followup > .sideInfo').hide();
});

$("#showAll").click(function (){
	$('.sideInfo').slideDown('fast');
});

$("#hideAll").click(function (){
	$('.sideInfo').slideUp('fast');
});

$('#comments > .sideHead').click(function() {
	$('#comments > .sideInfo').slideToggle('fast');
});

$('#timeoff > .sideHead').click(function() {
	$('#timeoff > .sideInfo').slideToggle('fast');
});

$('#unconfirmed > .sideHead').click(function() {
	$('#unconfirmed > .sideInfo').slideToggle('fast');
});

$('#followup > .sideHead').click(function() {
	$('#followup > .sideInfo').slideToggle('fast');
});
