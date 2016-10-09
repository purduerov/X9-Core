function Gamepad() {
  this.id = String;
  this.buttons = {
      a:      {pressed: false, index: Number},
      b:      {pressed: false, index: Number},
      x:      {pressed: false, index: Number},
      y:      {pressed: false, index: Number},
      lb:     {pressed: false, index: Number},
      rb:     {pressed: false, index: Number},
      lt:     {pressed: false, index: Number},
      rt:     {pressed: false, index: Number},
      slct:   {pressed: false, index: Number},
      strt:   {pressed: false, index: Number},
      rpress: {pressed: false, index: Number},
      lpress: {pressed: false, index: Number},
      up:     {pressed: false, index: Number},
      down:   {pressed: false, index: Number},
      left:   {pressed: false, index: Number},
      right:  {pressed: false, index: Number},
      length: 16
    };
  this.axes = {
      xleft:  {pos: Number, index: Number},
      yleft:  {pos: Number, index: Number},
      xright: {pos: Number, index: Number},
      yright: {pos: Number, index: Number},
      length: 4
    };
  this.ready = false;
}

var gp = new Gamepad();

var i_use = undefined;

var press_a_button = function(message) {
  if(message) {
console.log("true1");
    message.text("Press any button on the desired gamepad");
  } else {console.log("false");}
  var monitor = window.setInterval(function() {
    var chk = navigator.getGamepads();
    for(var i = 0; i < chk.length; i++) {
    console.log(chk.length +" "+i);
      if(chk[i] != undefined) {
        if(chk[i].buttons != undefined) {
          for(var j = 0; j < chk[i].buttons.length; j++) {
            if(chk[i].buttons[i].pressed) {
              window.clearInterval(monitor);
              if(i_use == undefined) {
                i_use = j;
              }
              if(message) {
                message.html("Gamepad connected!</br>ID: "+chk[i_use].id);
              }
              set_mapping(chk[i_use].id);
            }
          }
        }
      }
    }
  }, 100);
};

var set_mapping = function(id) {
  gp.id = id;
  Object.keys(layouts).forEach(function(key, i) {
    if(id == layouts[key].id) {
      Object.keys(layouts[key].buttons).forEach(function(key_b, i) {
        gp.buttons[key_b].index = layouts[key].buttons[key_b];
        gp.buttons[key_b].pressed = false;
      });
      Object.keys(layouts[key].axes).forEach(function(key_a, i) {
        gp.axes[key_a].index = layouts[key].axes[key_a];
      });
      gp.buttons.length = layouts[key].buttons.length;
      gp.axes.length = layouts[key].axes.length;
      gp.ready = true;
    }
  });
};

var get_buttons = function() {
  var read = navigator.getGamepads()[i_use];
  Object.keys(gp.buttons).forEach(function(key_b, i) {
    if(key_b != "length"){
      gp.buttons[key_b].pressed = read.buttons[gp.buttons[key_b].index].pressed;
      console.log("Buttons: "+gp.buttons[key_b].pressed+" "+key_b);
    }
  });
  Object.keys(gp.axes).forEach(function(key_a, i) {
    if(key_a != "length"){
      gp.axes[key_a].pos = read.axes[gp.axes[key_a].index];
      console.log("Axes: "+gp.axes[key_a]+" "+key_a);
    }
  });
}

