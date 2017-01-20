$(document).ready(function() {

	$(".employees tr:first").addClass("emp-head");
	$(".employees tr:even:not(tr:first)").addClass("emp-alt");
    // $( "a" ).click(function( event ) {
    //         alert( "The link will no longer take you to jquery.com" );
    //         event.preventDefault();
    //     });
    $( "a" ).click(function( event ) {
	    event.preventDefault();
    	$( this ).hide( "slow" );
 
});

});