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
                    var projectView = createCardView(data.title,data.subheading,data.url,data.description);
                    $('#stuff').append(projectView);
                    addWaypoint(projectView);
                    items.push(projectView);
                }
            });
        }
    }
    
    function createCardView(title, subheading, img, description){
        var projectView=$("<div/>");
        $(projectView).addClass("projectview col-md-5 col-xs-12 col-centered");
        projectView.attr('id',items.length);
        
        var subHeading=$('<h3/>').text(subheading);
        var titleView=$("<h1/>").text(title);
        
        var textWrapper = $('<div/>');
        $(textWrapper).addClass("cardTextWrapper");
        textWrapper.append(titleView);
        textWrapper.append(subHeading);
        
        var image=$("<img/>").addClass("projectimage");
        var imagewrapper=$("<div/>").addClass("imagewrapper");
        $(image).attr("src",img);
        $(imagewrapper).append(image);


        $(projectView).append(textWrapper);
        $(projectView).append(imagewrapper);
        
        $(projectView).click(function(e){
            var detailView = createDetailView(title,subheading,img, description);
            console.log(detailView);
            $('body').append(detailView);
        });
        return projectView;
    }
    
    function createDetailView(title,subheading,img, description){
        console.log(description);
        var mainView = $('<div/>');
        mainView.addClass('detailmain');
        var detailView = $('<div/>');
        $(detailView).addClass('detailView col-md-7 col-xs-12');
        
        var titleView = $('<h1/>');
        $(titleView).text(title);
        
        var subHeading = $('<h3/>');
        $(subHeading).text(subheading);
        
        var contentView = $('<div/>');
        contentView.addClass('detailContentView col-xs-12 col-md-12');
        
        var image=$("<img/>").addClass("detailprojectimage");
        image.attr('src',img);
        var imagewrapper=$("<div/>").addClass("detailimagewrapper");
        
        imagewrapper.append(image);
        
        var descriptionView = $('<p/>');
        $(descriptionView).text(description);
        
        contentView.append(imagewrapper);
        contentView.append(descriptionView);
        
        detailView.append(titleView);
        detailView.append(subHeading);
        detailView.append(contentView);
                
        mainView.append(detailView);
        return mainView;
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
