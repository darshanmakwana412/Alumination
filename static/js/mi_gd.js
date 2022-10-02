$('.counter').each(function() {
    var $this = $(this),
        countTo = $this.attr('data-count');
    
    $({ countNum: $this.text()}).animate({
      countNum: countTo
    },
  
    {
  
      duration: 1000,
      easing:'linear',
      step: function() {
        $this.text(Math.floor(this.countNum));
      },
      complete: function() {
        $this.text(this.countNum);
        //alert('finished');
      }
  
    });  
    
    
  
  });




$('#pref1').change(function(){
  if($('#pref1').val() == "Core + HR" || $('#pref2').val() == "Core + HR" || $('#pref3').val() == "Core + HR")
  {
  $("#coresub").attr("style", "display:block")
  }
  else{
    $("#coresub").attr("style", "display:none")
  }
})
$('#pref2').change(function(){
  if($('#pref1').val() == "Core + HR" || $('#pref2').val() == "Core + HR" || $('#pref3').val() == "Core + HR")

  {
  $("#coresub").attr("style", "display:block")
  }
  else{
    $("#coresub").attr("style", "display:none")
  }
})
$('#pref3').change(function(){
  if($('#pref1').val() == "Core + HR" || $('#pref2').val() == "Core + HR" || $('#pref3').val() == "Core + HR")

  {
  $("#coresub").attr("style", "display:block")
  }
  else{
    $("#coresub").attr("style", "display:none")
  }
})