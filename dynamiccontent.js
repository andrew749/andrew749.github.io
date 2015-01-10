$(document).ready(function(){
    var projectids=["play","heartratemonitor","textmetrics"/*,"secretsauce","myounlock","hive","scribblerplaystwitch"*/];

    function Entry(title, description, image){
        this.title=title;
        this.description=description;
        this.image=image;
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
                items.push( "<li id='" + data.title + "'>" + data.description + "</li>" );
                $( "<ul/>", {
                    "class": "my-new-list",
                    html: items.join( "" )
                }).appendTo( "body" );
            }
        });
    }

});