$(document).ready(function(){
  var items = [];
  var waypoint=[];
  addWaypoint(document.getElementById("textspam"));
  var projectids=["play","heartratemonitor","textmetrics","secretsauce","myomove","hive","scribblerplaystwitch","decisions", "0xFACE","tennisscore","drizio","panic.io","chordi"];
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
    var subHeading=$('<h3/>').text(subheading);
    var titleView=$("<h1/>").text(title);
    var textWrapper = $('<div/>');
    var image=$("<img/>").addClass("projectimage");
    var imagewrapper=$("<div/>").addClass("imagewrapper");
    $(textWrapper).addClass("cardTextWrapper");
    $(projectView).addClass("projectview col-md-5 col-xs-12 col-centered");
    $(image).attr("src",img);
    projectView.attr('id',items.length);
    $(imagewrapper).append(image);
    textWrapper.append(titleView);
    textWrapper.append(subHeading);
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

    var closeButton = $('<div/>');
    closeButton.addClass('closeButton');
    $(closeButton).click(function(e){
      $('.detailmain').remove();
    });
    $(closeButton).text('X');

    imagewrapper.append(image);

    var descriptionView = $('<p/>');
    $(descriptionView).text(description);

    contentView.append(imagewrapper);
    contentView.append(descriptionView);

    detailView.append(titleView);
    detailView.append(subHeading);
    detailView.append(contentView);
    detailView.append(closeButton);

    mainView.append(detailView);
    return mainView;
  }

  generateContent();

  function addWaypoint(element){
    $(element).addClass("hidecard");
    $(element).waypoint({
      element: element,
      handler: function() {
        $(this.element).removeClass("hidecard");
        $(this.element).addClass("animation");
      }
      ,
    offset:'70%'
    });
  };
});
