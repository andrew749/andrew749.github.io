$(document).ready(function(){
        var items = [];
    var waypoint=[];
    addWaypoint(document.getElementById("textspam"));
    var projectids=["play","heartratemonitor","textmetrics","secretsauce","myomove","hive","scribblerplaystwitch","decisions", "0xFACE","tennisscore","drizio","panic.io"];
    //spec for entry
    function Entry(title, description, url,subheading){
        this.title=title;
        this.description=description;
        this.url=url;
        this.subheading=subheading;
    }

    function generateContent(){
        //inflate the template and append to page
        for (var i in projectids){
            $.ajax({
                type: "GET",
                url: "content/"+projectids[i],
                dataType: "json" ,
                success: function (data) {
                    var projectView = createCardView(data.title,data.subheading,data.url);
                    $('#stuff').append(projectView);
                    addWaypoint(projectView);
                    items.push(projectView);
                }
            });
        }
    }
    
    function createCardView(title, subheading, img){
        var projectView=$("<div/>");
        $(projectView).addClass("projectview col-md-5 col-xs-12 col-centered");
        projectView.id=title.toLowerCase();
        
        var subHeading=$('<h3/>').text(subheading);
        var title=$("<h1/>").text(title);
        
        var textWrapper = $('<div/>');
        $(textWrapper).addClass("cardTextWrapper");
        textWrapper.append(title);
        textWrapper.append(subHeading);
        
        var image=$("<img/>").addClass("projectimage");
        var imagewrapper=$("<div/>").addClass("imagewrapper");
        $(image).attr("src",img);
        $(imagewrapper).append(image);


        $(projectView).append(textWrapper);
        $(projectView).append(imagewrapper);
        return projectView;
    }
    
    generateContent();
    
    function addWaypoint(element){
        $(element).addClass("hidecard");
        var tempwaypoint = new Waypoint({
            element: element,
            handler: function() {
                console.log("addingclass");
                $(this.element).removeClass("hidecard");
                $(this.element).addClass("animation");
            }
            ,
            offset:'70%'
        });

        waypoint.push(tempwaypoint);
    };


});
