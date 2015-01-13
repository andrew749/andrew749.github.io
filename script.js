$(document).ready(function(){
    //handles the image carousel
    var options = { $AutoPlay: true };
    var waypoints=[];
    var jssor_slider1 = new $JssorSlider$('slider1_container', options);
    $("#slider1_container").width("100%");
    //handles the button click to scroll the page
    $(".menubutton").on("click",function (event){
        //code for the event
        switch (event.delegateTarget.id){
            case "aboutbutton":
                clickHandler("#about");
                purgeClass();

                $("#aboutbutton").addClass("selectednavbutton");

                break;
            case "contactbutton":
                clickHandler("#contact");
                purgeClass();

                $("#contactbutton").addClass("selectednavbutton");

                break;
            case "homebutton":
                clickHandler("#home");
                purgeClass();

                $("#homebutton").addClass("selectednavbutton");

                break;

        }
    });
    $("#contactfab").click(function(){
        if($(".contactcardlayout").hasClass("contacthideinitial")){
            $(".contactcardlayout").removeClass("contacthideinitial");

        }
        if(!$(".contactcardlayout").hasClass("contacthide")){
            $(".contactcardlayout").addClass("contacthide");

        }else{
            $(".contactcardlayout").removeClass("contacthide").addClass("animation_slide_in");
        }


    });
    $("#emailcell").click(function(){
        window.location.href = "mailto:andrewcod749@gmail.com";


    });
    function clickHandler(id){
        console.log(id);
        $('html, body').animate({scrollTop: $(id).offset().top-100}, 500);
    }
    function purgeClass(){
        $("#aboutbutton").removeClass("selectednavbutton");
        $("#contactbutton").removeClass("selectednavbutton");
        $("#homebutton").removeClass("selectednavbutton");


    }
    //responsive code begin
    //you can remove responsive code if you don't want the slider scales
    //while window resizes
    function ScaleSlider() {
        var parentWidth = $('#slider1_container').parent().width();
        if (parentWidth) {
            jssor_slider1.$ScaleWidth(parentWidth/2);


        }
        else
            window.setTimeout(ScaleSlider, 30);
    }

    //Scale slider while window load/resize/orientationchange.
    $(window).bind("resize", ScaleSlider);
    $(window).bind("orientationchange", ScaleSlider);
    //responsive code end



    function slideInInformation(element){
        $(element).addClass("hidecard");
        var tempwaypoint = new Waypoint({
            element: element,
            handler: function() {
                $(this.element).removeClass("hidecard");
                $(this.element).addClass("animation_slide_in");
            }
            ,
            offset:'60%'
        });   
        waypoints.push(tempwaypoint);
    }
    var sections=document.getElementsByClassName('mainsection');
    for(var i in sections){
        slideInInformation(sections[i]);
        console.log(i);
    }

});
