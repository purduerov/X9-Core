/*
  This file creates a gp object -- the 'gamepad' -- and provides
  the library necessrily to fill it.
  
  Please include gp_layouts.js before gp_library.js in the html script tags.
  
  To set the gamepad/controller, use:
    controller.set();
    --note, you can pass an html element into this function to write
      its instructional messages to.
  
  To map the identified controller, use:
    controller.map()
    
    --The controller.map() function is called by controller.set(), although
      you are able to call it if you want to re-map gp.
  
  To get the status of the controller, once identified and mapped, use:
    controller.get_current():
  
    --I was going to separate out the processes for getting the button and
      axes statuses from each other, but we're going to be calling the status
      so quickly, I don't think it would be useful. Easy enough to make should
      we decide it is, however.

  
  To use the statuses of a button or a joystick, after using controller.get_current();,
  type reference it like so:
    A: gp.buttons.a.pressed           <- a true/false value for whether it's pressed or not
       gp.buttons.a.value           <- a 1/0 value for whether it's pressed or not (1 = true, 0 = false)
    
    left stick: gp.axes.xleft.pos    <- the position of the left joystick, x axis
                 gp.axes.yleft.pos    <- the position of the left joystick, y axis
    
    --to see what button lables are available, you can either look at gp_layouts.js, or 'inspect' your
      webpage and just type 'gp' in the command prompt there--it should show you the gp object, which you
      can click through to see its structure.
  
  
  All buttons and axis will have index values, which will be the same as in the gp_layouts.js file for the
  respective controller. This is mostly for reference within the functions in this file. Please don't edit them, you
  will need to call controller.map() again to reset any changes to the correct respective values.
*/

function Gamepad() {
  this.id = String;
  this.buttons = new Object;
  this.axes = new Object;
  this.ready = false;
}

var gp = new Gamepad();


var controller = {
  i_use: undefined,

  set: function(message) {
    if(message) {
      message.text("Press any button on the desired gamepad");
    }
    var monitor = window.setInterval(function() {
      var chk = navigator.getGamepads();
      for(var i = 0; i < chk.length; i++) {
        if(chk[i] != undefined) {
          if(chk[i].buttons != undefined) {
            for(var j = 0; j < chk[i].buttons.length; j++) {
              if(chk[i].buttons[i].pressed) {
                window.clearInterval(monitor);
                if(controller.i_use == undefined) {
                  controller.i_use = j;
                }
                if(message) {
                  message.html("Gamepad connected!</br>ID: "+chk[controller.i_use].id);
                }
                controller.map(chk[controller.i_use].id);
              }
            }
          }
        }
      }
    }, 100);
  },

  map: function(id) {
    gp.id = id;
    Object.keys(layouts).forEach(function(key, i) {
      if(id == layouts[key].id) {
        Object.keys(layouts[key].buttons).forEach(function(key_b, i) {
          if(key_b != "length") {
            gp.buttons[key_b] = {index: layouts[key].buttons[key_b], pressed: false};
          } else {
            gp.buttons[key_b] = layouts[key].buttons[key_b];
          }
        });
        Object.keys(layouts[key].axes).forEach(function(key_a, i) {
          if(key_a != "length") {
            gp.axes[key_a] = {index: layouts[key].axes[key_a], pos: Number};
          } else {
            gp.axes[key_a] = layouts[key].axes[key_a];
          }
        });
        gp.ready = true;
      }
    });
  },

  get_current: function() {
    read = navigator.getGamepads()[controller.i_use];
    Object.keys(gp.buttons).forEach(function(key_b, i) {
      if(key_b != "length"){
        gp.buttons[key_b].pressed = read.buttons[gp.buttons[key_b].index].pressed;
        gp.buttons[key_b].value = read.buttons[gp.buttons[key_b].index].value;
        //console.log("Buttons: "+gp.buttons[key_b].pressed+" "+key_b);
      }
    });
    Object.keys(gp.axes).forEach(function(key_a, i) {
      if(key_a != "length"){
        gp.axes[key_a].pos = read.axes[gp.axes[key_a].index];
        //console.log("Axes: "+gp.axes[key_a]+" "+key_a);
      }
    });
  }
}

