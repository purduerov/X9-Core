/*
**************************************************************************************************
  This file creates a gp object -- the 'gamepad' -- and provides
  the library necessrily to fill it.
  
  Please include gp_layouts.js before gp_library.js in the html script tags.
  
--------------------------------------------------------------------------------------------------
  To set the gamepad/gp, use:
    gp.set();
    --note, you can pass an html 'message' element into this function to write
      its instructional messages to.
  
--------------------------------------------------------------------------------------------------
  To map the identified gp, use:
    gp.map();
    
    --The gp.map() function is called by gp.set(), although
      you are able to call it if you want to re-map gp.
      
--------------------------------------------------------------------------------------------------
  To get the status of the gp, once identified and mapped, use:
    gp.get_current();
  
    --for best performance, I recommend this should be used inside of the master loop so
      there are no issues with asynchronous behavior.

--------------------------------------------------------------------------------------------------
  To use the statuses of a button or a joystick, after using gp.get_current();,
  type references to the gamepad like so:
    A: gp.buttons.a.val            <- a 1/0 value for whether it's pressed or not
       gp.buttons.a.pressed        <- a 1/0 value for if the button was just pressed or not
       gp.buttons.a.released       <- a 1/0 value for if the button was just released or not 
    
    left stick: gp.axes.left.x     <- the position of the left joystick, x axis
                gp.axes.left.y     <- the position of the left joystick, y axis
                gp.axes.left.r     <- the radius, or hypotenus of the triangle x and y make.
                gp.axes.left.theta <- the angle of the hypotenus from the y-axis (NOT x-axis)
                    --this functions the same as if you'd flipped the unit circle around the line y=x on the xy-plane
                
    --to see what button lables are available, you can either look at gp_layouts.js, or 'inspect' your
      webpage and just type 'gp' in the command prompt there--it should show you the gp object, which you
      can click through to see its structure.
**************************************************************************************************
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
  var but_func = new Object;
  
  this.butfuncreturn = function() {
    return but_func;
  }
  
  //these are for identifying if a button has just been pressed or released
  this.setButtonLast = function(key, init = false) { //is called right before updating buttons
    if(init) {                                       //init = true when gamepad is being mapped out; user shouldn't worry about it
      buttons_last[key] = {val: 0};
    } else {
      buttons_last[key].val = this.buttons[key].val;
    }
  };
  
  this.getButtonLastPress = function(key) { //allows for user to see/operate off of last press, if desired
    return buttons_last[key].val;
  };
  
  this.setStatusChange = function(key) { //this sets the pressed and released characteristics for each button
    if(this.buttons[key].val && !buttons_last[key].val) {
      this.buttons[key].pressed = 1;
      this.buttons[key].released = 0;
    } else if(!this.buttons[key].val && buttons_last[key].val) {
      this.buttons[key].pressed = 0;
      this.buttons[key].released = 1;
    } else {
      this.buttons[key].pressed = 0;
      this.buttons[key].released = 0;
    }
  };
  
  this.setDisplace = function(key, x, y) { //the initial value of the joysticks are considered their 'error'
    axes_off[key] = {"x": x, "y": y};
  };
  
  this.getDisplace = function() { //allows user to see what the displacement values are, if desired
    return axes_off;
  }
  
  this.axesAdjust = function(key, x, y) { //calculates the polar coordinates, and scales the axes based off of displacement
    var theta = 0;                        //because of the range of the joystick's possible error, the first 10% of movement
    var r = 0;                            //has been canceled out for now.
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
    
    theta = Math.atan2(x,y) * 180 / Math.PI;
    if(Math.abs(x) < .1 && Math.abs(y) < .1) {
      x = 0;
      y = 0;
      theta = 0;
    }
    
    r = Math.sqrt(x*x + y*y);
    
    if(r > 1) {
      r = 1;
    }
    
    return {"x": x, "y": y, "theta": theta, "r": r};
  }
  
  //string for btn and trigger, and function for func; i.e. this.bind("a", "change", function() {kill_all_humans} );
  //btn is the button key property of buttons, trigger can be 'change', 'press', or 'release'
  //arg is an object that holds the parameter 
  this.bind = function(btn, trigger, func, arg) {
    var func_key;
    var f_full;
    if(trigger == "change") {
      func_key = "change_func";
      f_full = function() {
        if(gp.buttons[btn].val != buttons_last[btn].val) {
          arg.message.text("hi");
          func(arg);
        }
      };
    } else if(trigger == "press") {
      func_key = "press_func";
      f_full = function() {
        if(gp.buttons[btn].pressed) {
          func(arg);
        }
      };
    } else if(trigger == "release") {
      func_key = "release_func";
      f_full = function() {
        if(gp.buttons[btn].released) {
          func(arg);
        }
      };
    }
    
    but_func[btn][func_key] = f_full;
    console.log(but_func[btn][func_key])
  }
  
  
  //these are for selecting the gamepad, mapping it from the library, and then updating the current status
  this.set = function(message) { //waits until it sees a gamepad with a button pressed, and sets it as the desired controller
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
                if(gp.i_use == undefined) {
                  gp.i_use = i;
                }
                if(message) {
                  message.html("Gamepad connected!</br>ID: "+chk[gp.i_use].id);
                }
                gp.map(chk[gp.i_use].id, message);
                //console.log("found a button press...");
              }
            }
          }
        }
      
        if(gp.ready) {                      //if gamepad matches a known layout, accept the chosen gamepad
          window.clearInterval(monitor);
          //console.log("gamepad accepted");
        }
      }
    }, 100);
  };

  this.map = function(id, message) { //
    gp.id = id;
    Object.keys(layouts).forEach(function(key, i) {
      if(id == layouts[key].id) {
        gp.layout = key;
        Object.keys(layouts[key].buttons).forEach(function(key_b, i) {
          if(key_b != "length") {
            gp.setButtonLast(key_b, true);
            gp.buttons[key_b] = {val: 0, pressed: 0, released: 0};
            but_func[key_b] = {change_func: null, press_func: null, release_func: null};
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
    if(!gp.ready && message) {
      message.html("The chosen gamepad did not match the library.");
    }
  };

  this.get_current = function(message) {
    read = navigator.getGamepads()[gp.i_use];
    if(read != undefined && gp.i_use != undefined) {
      Object.keys(gp.buttons) .forEach(function(key_b, i) {
        if(key_b != "length"){
          gp.setButtonLast(key_b);
          gp.buttons[key_b].val = read.buttons[layouts[gp.layout].buttons[key_b]].value;
          gp.setStatusChange(key_b);
          
          if(but_func[key_b].change_func != null) {
            but_func[key_b].change_func();
          }
          
          if(but_func[key_b].press_func != null) {
            but_func[key_b].press_func();
          }
          
          if(but_func[key_b].release_func != null) {
            but_func[key_b].release_func();
          }
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