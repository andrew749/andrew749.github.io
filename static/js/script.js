$(document).ready(function(){
  $(".button-collapse").sideNav();

  //handles the button click to scroll the page
  $(".menubutton").on("click",function (event){
    //code for the event
    purgeClass();
    switch (event.delegateTarget.id){
      case "aboutbutton":
        clickHandler("#about");
        $("#aboutbutton").addClass("selectednavbutton");
        break;
      case "contactbutton":
        clickHandler("#contact");
        $("#contactbutton").addClass("selectednavbutton");
        break;
      case "homebutton":
        clickHandler("#home");
        $("#homebutton").addClass("selectednavbutton");
        break;
    }
  });

  // helper to scroll to a particualr elmeent on the page
  function clickHandler(id){
    $('html, body').animate({scrollTop: $(id).offset().top-100}, 500);
  }

  // remove classes from selected buttons
  function purgeClass(){
    $("#aboutbutton").removeClass("selectednavbutton");
    $("#contactbutton").removeClass("selectednavbutton");
    $("#homebutton").removeClass("selectednavbutton");
  }

  // handle showing animation when client scrolls
  $.map( $('.main_section'), function (element) {
    $(element).addClass('hidecard');

    // add waypoint to all main elements
    $(element).waypoint( function () {
      // bind to this context
      $(this.element).removeClass("hidecard");
      $(this.element).addClass("animation_slide_in");
    } , {
      offset:'60%'
    }
    );

  });
});
