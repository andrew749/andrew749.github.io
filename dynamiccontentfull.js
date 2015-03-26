$(document).ready(function(){
    var items = [];
    var waypoint=[];
    //spec for entry
    function Entry(title, description, url,subheading,fields){
        this.title=title;
        this.description=description;
        this.url=url;
        this.subheading=subheading;
        //fields have a title, description and picture
        this.fields=fields;
    }
    function generateContent(){
        console.log("generate");
        //inflate the template and append to page
        $.ajax({
            type: "GET",
            url: "content/fullcontent/play",
            dataType: "json" ,
            success: function (data) {
                console.log(data);
                var fields=data.fields;
                //each field
                for( var k in fields){
                    var x=fields[k];
                    var t=x.title;
                    var s=x.subheading;
                    var i=x.url;
                    var d=x.description;
                    var item=$("<section/>");
                    var description=$("<p/>").text(d);
                    $(item).append($("<header/>").text(t));

                    $(item).append(description);
                    $(item).append($("<img/>").attr("src",i));
                    items.push(item);
                }
                $('body').append(items);
                //addWaypoint(projectView);
            },
            error: function (xhr, ajaxOptions, thrownError) {
                alert(xhr.status);
                alert(thrownError);
            }
        });
    }
    generateContent();


});
