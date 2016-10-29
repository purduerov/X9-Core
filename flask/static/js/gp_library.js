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
  this.i_use = undefined;
  var buttons_last = new Object;
  var axes_off = new Object;
  
  //these are for identifying if a button has just been pressed or released
  this.setButtonLast = function(key, init) { //is called right before updating buttons
    if(init) {
      buttons_last[key] = init;
    } else {
      buttons_last[key].pressed = this.buttons[key].val;
    }
  };
  
  this.getButtonLastPress = function(key) {
    return buttons_last[key].pressed;
  };
  
  this.setStatusChange = function(key) {
    if(this.buttons[key].val && !(this.getButtonLastPress(key))) {
      this.buttons[key].pressed = 1;
      this.buttons[key].released = 0;
    } else if(!this.buttons[key].val && this.getButtonLastPress(key)) {
      this.buttons[key].pressed = 0;
      this.buttons[key].released = 1;
    } else {
      this.buttons[key].pressed = 0;
      this.buttons[key].released = 0;
    }
  };
  
  this.setDisplace = function(key, x, y) {
    axes_off[key] = {"x": x, "y": y};
  };
  
  this.getDisplace = function() {
    return axes_off;
  }
  
  this.axesAdjust = function(key, x, y) {
    var theta = 0;
    var r = 0;
    if(x > 0) {
      x = (x - axes_off[key].x) / (1 - axes_off[key].x);
    } else {
      x = (x - axes_off[key].x) / (1 + axes_off[key].x);
    }
    
    if(y > 0) {
      y = -(y - axes_off[key].y) / (1 - axes_off[key].y);
    } else {
      y = -(y - axes_off[key].y) / (1 + axes_off[key].y);
    }
    
    theta = Math.atan2(x,-y) * 180 / Math.PI;
    if(Math.abs(x) < .1 && Math.abs(y) < .1) {
      x = 0;
      y = 0;
      theta = 0;
    }
    
    r = x / Math.cos(theta) * 180 / Math.PI;
    
    return {"x": x, "y": y, "theta": theta, "r": r};
  }
  
  
  
  
  //these are for selecting the gamepad, mapping it from the library, and then updating the current status
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
                gp.map(chk[gp.i_use].id, message);
              }
            }
          }
        }
      }
    }, 100);
  };

  this.map = function(id, message) {
    gp.id = id;
    Object.keys(layouts).forEach(function(key, i) {
      if(id == layouts[key].id) {
        gp.layout = key;
        Object.keys(layouts[key].buttons).forEach(function(key_b, i) {
          if(key_b != "length") {
            gp.setButtonLast(key_b, {pressed: 0, released: 0});
            gp.buttons[key_b] = {val: 0, pressed: 0, released: 0};
          } else {
            gp.buttons[key_b] = layouts[key].buttons[key_b];
          }
        });
        var arrays = navigator.getGamepads()[gp.i_use].axes;
        Object.keys(layouts[key].axes).forEach(function(key_a, i) {
          if(key_a != "length") {
            gp.setDisplace(key_a, arrays[layouts[gp.layout].axes[key_a].x], arrays[layouts[gp.layout].axes[key_a].y]);
            gp.axes[key_a] = {x: 0, y: 0, theta: 0, r: 0};
          } else {
            gp.axes[key_a] = layouts[key].axes[key_a];
          }
        });
        gp.ready = true;
      }
    });
    // if(!gp.ready && message) {
      // message.html("The chosen gamepad did not match the library.");
    // }
  };

  this.get_current = function(message) {
    read = navigator.getGamepads()[gp.i_use];
    if(read != undefined && gp.i_use != undefined) {
      Object.keys(gp.buttons) .forEach(function(key_b, i) {
        if(key_b != "length"){
          gp.setButtonLast(key_b);
          gp.buttons[key_b].val = read.buttons[layouts[gp.layout].buttons[key_b]].value;
          gp.setStatusChange(key_b);
          //console.log("Buttons: "+gp.buttons[key_b].press+" "+key_b);
        }
      });
//console.log(gp.buttons.down.val+" "+gp.buttons.down.released);
      Object.keys(gp.axes).forEach(function(key_a, i) {
        if(key_a != "length"){
          gp.axes[key_a] = gp.axesAdjust(key_a, read.axes[layouts[gp.layout].axes[key_a].x], read.axes[layouts[gp.layout].axes[key_a].y]);
          //console.log("Axes: "+gp.axes[key_a].pos+" "+key_a);
        }
      });
      
    } else {
      Object.keys(gp.buttons) .forEach(function(key_b, i) {
        if(key_b != "length"){
          gp.buttons[key_b].val = 0;            //let go of all buttons
          //console.log("Buttons: "+gp.buttons[key_b].press+" "+key_b);
        }
      });
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
  };
}

var gp = new Gamepad();