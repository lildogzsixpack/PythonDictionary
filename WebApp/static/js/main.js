// $(document).on("submit", "#wordForm", function(e) {
// 	e.preventDefault();

//     var form = $(this);
//     console.log(result);
//     var stringData = JSON.stringify(result);
//     $.ajax({
//         url: form.attr('action'),
//         method: form.attr('method'),
//         data: result,
//         contentType: 'application/json;charset=UTF-8',
//         dataType: "json",
//         success:function (result) {
//         	$("#input").val("");
//         	console.log(result);
//         	}
//         });
//     });


$( "#search" ).autocomplete({
    source: function( request, response ) {
		var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
		response( $.grep( words, function( item ){
		return matcher.test( item );
        }) );
      }
});