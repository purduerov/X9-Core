$(document).ready(function() {
  setInterval(function() {
    var gp = navigator.getGamepads();
    var div = $("#moving");
    var mes = $("#messages");

    gp = navigator.getGamepads();
    if(gp != null && gp != undefined) {
      gp.a = gp[0].buttons[0].pressed;
      gp.b = gp[0].buttons[1].pressed;
      gp.x_ax = gp[0].axes[0];
      gp.y_ax = gp[0].axes[1];
      mes.text("A: "+gp.a+"    B: "+gp.b+"    X-axis: "+parseInt(gp.x_ax*10)+"    Y-axix: "+parseInt(gp.y_ax*10));

      if(gp.a && !gp.b) {
        div.css("background-color", "cyan");
      } else if(gp.b && !gp.a) {
        div.css("background-color", "red");
      }

      

      div.css({top: "+="+parseInt(10*gp.y_ax)+"px"});
      div.css({left: "+="+parseInt(10*gp.x_ax)+"px"});
    } else {
      mes.text("No Gamepads Found");
    }
  }, 1);
});
