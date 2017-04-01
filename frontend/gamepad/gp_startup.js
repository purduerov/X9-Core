var go1 = -1;
var go2 = -1;
/*var data = {}
data.imu = {}

var set_imu = function(){
  data.imu.z = gp.buttons.a.val - gp.buttons.b.val
  data.imu.x = gp.axis.right.x
  data.imu.y = gp.axis.right.y
}

Can't make 'data' here?
"Uncaught ReferenceError: data is not defined at <anonymous>:1:1"
  ^is thrown to the console when I try to access 'data' on Chrome
*/

var run = function(abt) {
  if(gp.ready) {
    bind.activate();
    window.clearInterval(go1);
    go1 = -1;
    go2 = window.setInterval(function() {
      gp.get_current();
/*      set_imu();
      if(gp.ready) {
        active_div();
      } else {
        $("#reset").click();
      }
  ---this is the auto-reset method I had tied into the test file for the gamepad---
 */   }, 10);
  }
}

$(document).ready(function() {
//  var abt = $("#titles");
  gp.set();

  go1 = window.setInterval(function() { run(); }, 50);


/*  $("#reset").click(function() {
    if(go2 != -1) {
      gp.ready = false;
      window.clearInterval(go2);
      go2 = -1
    } else {console.log("go2: "+go2+" go1: "+go1);}
    $("#info").empty();
    gp.set();
    go1 = window.setInterval(function() { run(); }, 50);
  });
---keeping this more as notes for when we apply a reset/autoreset application to the webpage---
*/
});
