jQuery(function($) {
	$("select#id_form_language").change(function(e) {
	    window.location="?form_language="+this.value;
	});
});
