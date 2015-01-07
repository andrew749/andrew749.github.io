$(document).ready(function(){
    var waypoint=[];
    for( i=0;i<1000;i++){
        $(".container").append("<div class=\"card hidecard\" id=\""+i+"\">"+i+"</div>");
        var tempwaypoint = new Waypoint({
            element: document.getElementById(i),
            handler: function() {
                console.log("addingclass");
                $(this.element).removeClass("hidecard");
                $(this.element).addClass("animation");
            }
            ,
            offset:'80%'
        });

        waypoint.push(tempwaypoint);
    }


});
