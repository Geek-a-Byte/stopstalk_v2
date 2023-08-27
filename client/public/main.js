
window.onload = function(){
  const percent = document.getElementById('percent');
  var val = parseInt($(percent).val())/1200*100;
  val=val.toFixed(2);
  // var calc=val*100;
  // var val = calc;
  var $circle = $('#svg #bar');
  
  if (isNaN(val)) {
   val = 100; 
  }
  else{
    var r = $circle.attr('r');
    var c = Math.PI*(r*2);
   
    if (val < 0) { val = 0;}
    if (val > 100) { val = 100;}
    
    var pct = ((100-val)/100)*c;
    
    $circle.css({ strokeDashoffset: pct});
    
    $('#cont').attr('data-pct', parseInt($(percent).val()));
    $('#cont2').attr('data-pct2', val);
  }
}
