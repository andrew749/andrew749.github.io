$(document).ready(function(){
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
    $("#contactfab").on("click",function(event){
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
        $('html, body').animate({scrollTop: $(id).offset().top-100}, 500);
    }
    function purgeClass(){
        $("#aboutbutton").removeClass("selectednavbutton");
        $("#contactbutton").removeClass("selectednavbutton");
        $("#homebutton").removeClass("selectednavbutton");
    }
    function slideInInformation(element){
        $(element).addClass("hidecard");
        $(element).waypoint({
            element: element,
            handler: function() {
                $(this.element).removeClass("hidecard");
                $(this.element).addClass("animation_slide_in");
            }
            ,
            offset:'60%'
        });
    }
    var sections = document.getElementsByClassName('mainsection');
    for(var i in sections) {
        slideInInformation(sections[i]);
    }
});
