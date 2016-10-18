/*
  This file creates a gp object -- the 'gamepad' -- and provides
  the library necessrily to fill it.
  
  Please include gp_layouts.js before gp_library.js in the html script tags.
  
  To set the gamepad/gp, use:
    gp.set();
    --note, you can pass an html element into this function to write
      its instructional messages to.
  
  To map the identified gp, use:
    gp.map()
    
    --The gp.map() function is called by gp.set(), although
      you are able to call it if you want to re-map gp.
  
  To get the status of the gp, once identified and mapped, use:
    gp.get_current():
  
    --I was going to separate out the processes for getting the button and
      axes statuses from each other, but we're going to be calling the status
      so quickly, I don't think it would be useful. Easy enough to make should
      we decide it is, however.

  
  To use the statuses of a button or a joystick, after using gp.get_current();,
  type reference it like so:
    A: gp.buttons.a.press            <- a true/false value for whether it's pressed or not
       gp.buttons.a.val              <- a 1/0 value for whether it's pressed or not (1 = true, 0 = false)
    
    left stick: gp.axes.xleft.pos    <- the position of the left joystick, x axis
                gp.axes.yleft.pos    <- the position of the left joystick, y axis
    
    --to see what button lables are available, you can either look at gp_layouts.js, or 'inspect' your
      webpage and just type 'gp' in the command prompt there--it should show you the gp object, which you
      can click through to see its structure.
*/

function Gamepad() {
  this.id = String;
  this.layout = String;
  this.buttons = new Object;
  this.axes = new Object;
  this.ready = false;
  this.i_use = undefined,

  this.set = function(message) {
    if(message) {
      message.text("Press any button on the desired gamepad");
    }
    var monitor = window.setInterval(function() {
      var chk = navigator.getGamepads();
      for(var i = 0; i < chk.length; i++) {
        if(chk[i] != undefined) {
          if(chk[i].buttons != undefined) {
            for(var j = 0; j < chk[i].buttons.length; j++) {
              if(chk[i].buttons[j].pressed) {
                window.clearInterval(monitor);
                if(gp.i_use == undefined) {
                  gp.i_use = i;
                }
                if(message) {
                  message.html("Gamepad connected!</br>ID: "+chk[gp.i_use].id);
                }
                gp.map(chk[gp.i_use].id);
              }
            }
          }
        }
      }
    }, 100);
  },

  this.map = function(id) {
    gp.id = id;
    Object.keys(layouts).forEach(function(key, i) {
      if(id == layouts[key].id) {
        gp.layout = key;
        Object.keys(layouts[key].buttons).forEach(function(key_b, i) {
          if(key_b != "length") {
            gp.buttons[key_b] = {press: false, val: 0};
          } else {
            gp.buttons[key_b] = layouts[key].buttons[key_b];
          }
        });
        Object.keys(layouts[key].axes).forEach(function(key_a, i) {
          if(key_a != "length") {
            gp.axes[key_a] = {pos: Number};
          } else {
            gp.axes[key_a] = layouts[key].axes[key_a];
          }
        });
        gp.ready = true;
      }
    });
  },

  this.get_current = function(message) {
    read = navigator.getGamepads()[gp.i_use];
    if(read != undefined && gp.i_use != undefined) {
      Object.keys(gp.buttons) .forEach(function(key_b, i) {
        if(key_b != "length"){
          gp.buttons[key_b].press = read.buttons[layouts[gp.layout].buttons[key_b]].pressed;
          gp.buttons[key_b].val = read.buttons[layouts[gp.layout].buttons[key_b]].value;
          //console.log("Buttons: "+gp.buttons[key_b].press+" "+key_b);
        }
      });
      Object.keys(gp.axes).forEach(function(key_a, i) {
        if(key_a != "length"){
          gp.axes[key_a].pos = read.axes[layouts[gp.layout].axes[key_a]];
          //console.log("Axes: "+gp.axes[key_a].pos+" "+key_a);
        }
      });
      
    } else {
      Object.keys(gp.buttons) .forEach(function(key_b, i) {
        if(key_b != "length"){
          gp.buttons[key_b].press = false;
          gp.buttons[key_b].val = 0;
          //console.log("Buttons: "+gp.buttons[key_b].press+" "+key_b);
        }
      });
  //Depending on how we design button presses to communicate with the tools... we can either keep 
  //  the last button press status, or reset them all.
      Object.keys(gp.axes).forEach(function(key_a, i) {
        if(key_a != "length"){
          gp.axes[key_a].pos = 0;               //don't want to run the ROV into a wall if the gamepad disconnects
          //console.log("Axes: "+gp.axes[key_a].pos+" "+key_a);
        }
      });
      gp.ready = false;                       //gp is no longer ready **can be used in outer loop for a marker**
      gp.i_use = undefined;                   //to reconnect, we'll have to re-assign where the valid gamepad is
      if(message != undefined) {
        message.text("Gamepad disconnected");
      }
    }
  }
}

var gp = new Gamepad();