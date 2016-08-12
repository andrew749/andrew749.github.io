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
});
