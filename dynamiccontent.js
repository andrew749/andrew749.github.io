$(document).ready(function(){
    var projectids=["play","heartratemonitor","textmetrics","secretsauce","myomove","hive","scribblerplaystwitch"];
    //spec for entry
    function Entry(title, description, url,subheading){
        this.title=title;
        this.description=description;
        this.url=url;
        this.subheading=subheading;
    }
    var items = [];

    //inflate the template and append to page
    for (var i in projectids){
        $.ajax({
            type: "GET",
            url: "content/"+projectids[i],
            dataType: "json" ,
            success: function (data) {
                console.log(data);
                var element="<div class=\"projectview col-md-5 \" id=\""+data.title.toLowerCase()+"\"><h1>"+data.title+"</h1><h3>"+data.subheading+"</h3><br /><br /><div class=\"imagewrapper\"><img class=\"projectimage\" src=\""+data.url+"\"/></div><div class=\"projectdescription\"><p>"+data.description+"</p></div></div>"
                items.push(element);
                $('#stuff').append(element);

            }
        });
    }

});