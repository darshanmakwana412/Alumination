navshow = false
    
$('#hamburger').click(function(){
    $(this).toggleClass('open')
    navshow = !navshow
    if(navshow) $('#overlay').animate({height:$(window).height()},200);
    else $('#overlay').animate({height:0},200);
    
  })

  $('#overlay ul li').click(function(){
    $('#overlay').animate({height:0},200);
    navshow = false
    $('#hamburger').toggleClass('open')
    
  })
