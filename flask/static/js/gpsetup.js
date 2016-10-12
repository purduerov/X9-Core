var i_use = undefined;

var chooseGamepad = function(mes) {
  var gp = navigator.getGamepads();
  var i = 0;
  
  while(i < gp.length && i_use == undefined){
    if(gp[i] != undefined) {
      if(gp[i].buttons[0] != undefined) {
        if(gp[i].buttons[0].pressed) {
          i_use = i;
          
        }
      }
    }
    i++;
  }
  
  return i_use;
}

var registerGP = function(mes) {
  mes.text("Press 'A' on the Gamepad you want to use");
  
  var getGP = window.setInterval(function(i_use) {
    i_use = chooseGamepad(mes, i_use);
    
  if(i_use != undefined) {
    window.clearInterval(getGP);
    mes.text("Gamepad connected at Index "+i_use+"!");
  }
  }, 10);
}

$(document).ready(function() {
  var mes = $("#messages");
  
  i_use = registerGP(mes);
  
  var print = window.setInterval(function() {
    if(i_use) {
      console.log(i_use);
      window.clearInterval(print);
    }
  });
});