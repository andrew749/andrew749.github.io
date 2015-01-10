$(document).ready(function(){
        var items = [];
    var waypoint=[];
    addWaypoint(document.getElementById("textspam"));
    var projectids=["play","heartratemonitor","textmetrics","secretsauce","myomove","hive","scribblerplaystwitch"];
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
                    console.log(data);
                    var projectView=$("<div/>");
                    $(projectView).addClass("projectview col-md-5");
                    projectView.id=data.title.toLowerCase();
                    var subHeading=$('<h3/>').text(data.subheading);
                    var description=$("<p/>").text(data.description);
                    var descriptionWrapper=$("<div/>");
                    $(descriptionWrapper).append(description);
                    $(descriptionWrapper).addClass("projectdescription");
                    var image=$("<img/>").addClass("projectimage");
                    var imagewrapper=$("<div/>").addClass("imagewrapper");
                    $(image).attr("src",data.url);
                    $(imagewrapper).append(image);

                    var title=$("<h1/>").text(data.title);
                    $(projectView).append(title);
                    $(projectView).append(subHeading);
                    $(projectView).append(imagewrapper);
                    $(projectView).append(descriptionWrapper);
                    items.push(projectView);
                    $('#stuff').append(projectView);
                    addWaypoint(projectView);
                }
            });
        }
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