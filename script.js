$(document).ready(function(){
	//handles the image carousel
	var options = { $AutoPlay: true };
  var jssor_slider1 = new $JssorSlider$('slider1_container', options);
	//handles the button click to scroll the page
	$(".menubutton").on("click",function (event){
		//code for the event
		switch (event.delegateTarget.id){
			case "aboutbutton":
				clickHandler("#about");
				break;
			case "contactbutton":
				clickHandler("#contact");
				break;
			case "homebutton":
				clickHandler("#");
				break;

		}
	});
	function clickHandler(id){
		$('html, body').animate({scrollTop: $(id).offset().top}, 2000);
	}
});
