
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