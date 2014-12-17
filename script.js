$(document).ready(function(){
	//handles the image carousel
	var options = { $AutoPlay: true };
  var jssor_slider1 = new $JssorSlider$('slider1_container', options);
	$("#slider1_container").width("512px");
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
				clickHandler("#home");
				break;

		}
	});
	$("#contactfab").click(function(){
			$(".contactcardlayout").toggleClass("contacthide");

	});
	$("#emailcell").click(function(){
		window.location.href = "mailto:andrewcod749@gmail.com";


	});
	function clickHandler(id){
		console.log(id);
		$('html, body').animate({scrollTop: $(id).offset().top-100}, 2000);
	}
});
