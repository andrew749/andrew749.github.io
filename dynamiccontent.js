$(document).ready(function(){
    var projectids=["play","heartratemonitor","textmetrics","secretsauce","myomove","hive","scribblerplaystwitch"];
    //spec for entry
    function Entry(title, description, image,subheading){
        this.title=title;
        this.description=description;
        this.image=image;
        this.subheading=subheading;
    }
        //inflate the template and append to page
        for (var i in projectids){
            $.ajax({
                type: "GET",
                url: "content/"+projectids[i],
                dataType: "json" ,
                success: function (data) {
                    console.log(data);
                    var items = [];
                    items.push( "<li id='" + data.title + "'>" +data.title+"<br>Subheading:"+data.subheading+"<br> Description:"+ data.description + "</li>" );
                    $( "<ul/>", {
                        "class": "my-new-list",
                        html: items.join( "" )
                    }).appendTo( "body" );
                }
            });
        }

    });