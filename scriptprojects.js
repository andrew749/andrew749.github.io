$(document).ready(function(){
    var waypoint=[];
    var projectids=["textspam","play","heartratemonitor","textmetrics","secretsauce","myounlock","hive","scribblerplaystwitch"];
    projectids.forEach(function(entry){
        var ele=document.getElementById(entry);
        $(ele).addClass("hidecard");
        var tempwaypoint = new Waypoint({
            element: ele,
            handler: function() {
                console.log("addingclass");
                $(this.element).removeClass("hidecard");
                $(this.element).addClass("animation");
            }
            ,
            offset:'70%'
        });

        waypoint.push(tempwaypoint);
    });

});
