$(document).ready(function(){
  $('.detailmain').each(function() {
    var view = this;
    $('.closeButton').click(function(){
      $(view).addClass('hidden');
    });
  });

  $('.project').click(function(e){
    $(this).next().removeClass('hidden');
  });

  // for each project
  $.map( $('.project'), function(element) {
    $(element).addClass('hidecard');
    $(element).waypoint( function () {
      $(this.element).removeClass('hidecard');
      $(this.element).addClass('animation_slide_up');
    }, {
      offset: '90%'
    });
  });

});
