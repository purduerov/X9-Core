$(document).ready(function() {
  var messages = $("#messages");
  press_a_button(messages);
  
  var go = window.setInterval(function() {
    if(gp.ready) {
      window.clearInterval(go);
      console.log("clear");
      get_buttons();
      if(gp.buttons.a.pressed == true) {
        $("#moving").css("background-color", "cyan");
      } else {
        $("#moving").css("background-color", "green");
      }
    }
  }, 10);
});