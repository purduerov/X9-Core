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
  this.axes = {left: {}, right: {}};
  this.b_len = 0;
  this.a_len = 0;
  this.ready = false;
  this.i_use = undefined;
  var buttons_last = new Object;
  var axes_off = new Object;
  var but_func = new Object;
  var ax_func = {left: null, right: null};
  
  this.butfuncexist = function(key) {
    return but_func[key] != undefined;
  };
  
  this.butfuncreturn = function() {
    return but_func;
  };
  
  this.axfuncexist = function(key) {
    return ax_func[key] != undefined;
  };
  
  this.axfuncreturn = function() {
    return ax_func;
  };
  
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
  
  //string for btn and trigger, and function for func; i.e. this.btn_bind("a", "change", function() {kill_all_humans} );
  //btn is the button key property of buttons, trigger can be 'value', 'change', 'press', or 'release'
  //------value = while it's being pressed, press = first instant it gets pressed
  //arg is an object that holds the parameter
  /* -----FUNCTION assumed to depend on when status turns TRUE----- */
  this.btn_bind = function(btn, trigger, func, arg) {
    var bfunc_key = null;
    var bf_full = null;
    if(trigger == "change") {
      bfunc_key = "change_func";
      bf_full = function() {
        if(gp.buttons[btn].val != buttons_last[btn].val) {
          func(arg);
        }
      };
    } else if(trigger == "value") {
      bfunc_key = "val_func";
      bf_full = function() {
        if(gp.buttons[btn].val){
          func(arg);
        }
      }
    } else if(trigger == "press") {
      bfunc_key = "press_func";
      bf_full = function() {
        if(gp.buttons[btn].pressed) {
          func(arg);
        }
      };
    } else if(trigger == "release") {
      bfunc_key = "release_func";
      bf_full = function() {
        if(gp.buttons[btn].released) {
          func(arg);
        }
      };
    }
    
    if(bf_full != null && bfunc_key != null) {
      but_func[btn][bfunc_key] = bf_full;
      //console.log(but_func[btn][bfunc_key]);
    }
  }
  
  //string for side and trigger, and function for func; i.e. this.ax_bind("left", "polar", function() {kill_all_humans} );
  //side is the button key property of buttons, trigger can be 'polar' or 'cartesian'
  //arg is an object that holds the parameter
  /* -----FUNCTION assumed to work for ANY VALUE given by joysticks----- */
  this.ax_bind = function(side, trigger, func, arg) {
    var afunc_key = null;
    if(trigger == "polar") {
      afunc_key = "polar_func";
      
    } else if(trigger == "cartesian") {
      afunc_key = "cartes_func";
    }
    
    if(afunc_key != null) {
      //console.log("Binding: "+side+" "+afunc_key);
      ax_func[side][afunc_key] = function() {
        func(arg);
      }
      //console.log(ax_func[side][afunc_key]);
    }
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

  this.map = function(id, message) { //maps the gamepad, and the related functions unless they've been defined for the button before
    gp.id = id;
    Object.keys(layouts).forEach(function(key, i) {
      Object.keys(layouts[key].id).forEach(function(id, j) {
      if(id == layouts[key][id]) {
        gp.layout = key;
        gp.b_len = layouts[key].buttons.length;
        var name = "";
        for(var i = 0; i < gp.b_len; i++) {
          name = layouts[key].buttons[i].name;
          gp.setButtonLast(name, true);
          gp.buttons[name] = {val: 0, pressed: 0, released: 0};
          if(but_func[name] == undefined) {
            but_func[name] = {val_func: null, change_func: null, press_func: null, release_func: null};
          }
        }
        var arrays = navigator.getGamepads()[gp.i_use].axes;
        var cur_index = -1;
        var which = "";
        gp.a_len = layouts[key].axes.length;
        for(var i = 0; i < gp.a_len; i++) {
          name = layouts[key].axes[i].name;
          which = layouts[key].axes[i].which;
          cur_index = layouts[key].axes[i].index;
          gp.axes[which][name] = arrays[cur_index];
          if(ax_func[name] == undefined) {
            ax_func[which] = {polar_func: null, cartes_func: null};
          }
        }
        gp.setDisplace("left", gp.axes.left.x, gp.axes.left.y);
        gp.setDisplace("right", gp.axes.right.x, gp.axes.right.y);
        gp.ready = true;
      }
      });
    });
    if(!gp.ready && message) {
      message.html("The chosen gamepad did not match the library.");
    }
  };

  this.get_current = function(message) {
    read = navigator.getGamepads()[gp.i_use];
    if(read != undefined && gp.i_use != undefined) {
      var name = "";
      var where = "";
      var cur_index = -1;
      for(var i = 0; i < gp.b_len; i++) {
          name = layouts[gp.layout].buttons[i].name;
          where = layouts[gp.layout].buttons[i].where;
          cur_index = layouts[gp.layout].buttons[i].index;
          gp.setButtonLast(name);
          if(where == "buttons") {
            gp.buttons[name].val = (read[where][cur_index].value == layouts[gp.layout].buttons[i].match)? 1 : 0;
          } else if (where == "axes") {
            gp.buttons[name].val = (read[where][cur_index] == layouts[gp.layout].buttons[i].match)? 1 : 0;
          } else {
            console.log("Error: "+where+" presented instead of 'buttons' or 'axes' for get_current in gp_library.js")
          }
          gp.setStatusChange(name);
          
          if(but_func[name].change_func != null) {
            but_func[name].change_func();
          }
          
          if(but_func[name].val_func != null) {
            but_func[name].val_func();
          }
          
          if(but_func[name].press_func != null) {
            but_func[name].press_func();
          }
          
          if(but_func[name].release_func != null) {
            but_func[name].release_func();
          }
          //console.log("Buttons: "+gp.buttons[name].press+" "+name);
      }
//console.log(gp.buttons.down.val+" "+gp.buttons.down.released);
      var temp_axes = {left: {x: 0, y: 0}, right: {x: 0, y: 0}};
      for(var i = 0; i < gp.a_len; i++) {
          name = layouts[gp.layout].axes[i].name;
          which = layouts[gp.layout].axes[i].which;
          cur_index = layouts[gp.layout].axes[i].index;
          
          temp_axes[which][name] = read.axes[cur_index];
      }
        
      Object.keys(gp.axes).forEach(function(key_a, i) {
          gp.axes[key_a] = gp.axesAdjust(key_a, temp_axes[key_a].x, temp_axes[key_a].y);
          if(ax_func[key_a].polar_func != null) {
            ax_func[key_a].polar_func();
          }
          
          if(ax_func[key_a].cartes_func != null) {
            ax_func[key_a].cartes_func();
          }
          //console.log("Axes: "+gp.axes[key_a].pos+" "+key_a);
      });
      
    } else {
      Object.keys(gp.buttons).forEach(function(key_b, i) {
          Object.keys(gp.buttons[key_b]).forEach(function(butn_bit, j) {
            gp.buttons[key_b][butn_bit] = 0;            //let go of all buttons
          });
          //console.log("Buttons: "+gp.buttons[key_b].press+" "+key_b);
      });
      Object.keys(gp.axes).forEach(function(key_a, i) {
          Object.keys(gp.axes[key_a]).forEach(function(ax_bit, j) {
            gp.axes[key_a][ax_bit] = 0;               //don't want to run the ROV into a wall if the gamepad disconnects
          });
          //console.log("Axes: "+gp.axes[key_a].pos+" "+key_a);
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