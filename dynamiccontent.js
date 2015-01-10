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
            url: "http://andrewcodispoti.me/content/"+projectids[i],
            dataType: "json" ,
            success: function (data) {
                var items = [];
                $.each( data, function( key, val ) {
                    items.push( "<li id='" + key + "'>" + val + "</li>" );
                    console.log(key+":"+value+"\n");
                });

                $( "<ul/>", {
                    "class": "my-new-list",
                    html: items.join( "" )
                }).appendTo( "body" );
            }
        });
    }

});