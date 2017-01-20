/*
  Each button can have one of four function types {value, change, press, release}, which
  will each have a func property and a params OBJECT property to go along with it.
  
  button template:
    btn: {
      value: {
        params: undefined,
        func: null,
      },
      change: {
        params: undefined,
        func: null, 
      },
      press: {
        params: undefined,
        func: null, 
      },
      release: {
        params: undefined,
        func: null, 
      },
    },
    
  Each axes can have one of two function types {cartesian, polar}, which
  will each have a func function property and a params OBJECT property to go along with it.
  
  axes template:
    side: {
      cartesian: {
        params: undefined,
        func: null,
      },
      polar: {
        params: undefined,
        func: null,
      },
    },
*/

bind = {
  btn: {
    a: {
      press: {
        func: function() {
          console.log(packet.IMU.z);
          packet.IMU.z = gp.buttons.a.val;
        },  
      },
      release: {
        func: function() {
          console.log(packet.IMU.z);
          if(packet.IMU.z > 0) {
            packet.IMU.z = 0;
          }
        },
      },
    },
    b: {
      press: {
        func: function() {
          console.log(packet.IMU.z);
          packet.IMU.z = -gp.buttons.b.val;
        }, 
      },
      release: {
        func: function() {
          console.log(packet.IMU.z);
          if(packet.IMU.z < 0) {
            packet.IMU.z = 0;
          }
        }, 
      },
    },
    lb: {
      press: {
        func: function() {
          console.log(packet.IMU.roll);
          packet.IMU.roll = -gp.buttons.lb.val;
        },  
      },
      release: {
        func: function() {
          console.log(packet.IMU.roll);
          if(packet.IMU.roll < 0) {
            packet.IMU.roll = 0;
          }
        },
      },
    },
    rb: {
      press: {
        func: function() {
          console.log(packet.IMU.roll);
          packet.IMU.roll = gp.buttons.rb.val;
        }, 
      },
      release: {
        func: function() {
          console.log(packet.IMU.roll);
          if(packet.IMU.roll > 0) {
            packet.IMU.roll = 0;
          }
        }, 
      },
    },
    
  },
  ax: {
    left: {
      cartesian: {
        func: function() {
          packet.IMU.y = gp.axes.left.x;
          packet.IMU.x = gp.axes.left.y;
        },
      },
    },
    right: {
      cartesian: {
        func: function() {
          packet.IMU.pitch = gp.axes.right.y;
          packet.IMU.yaw = gp.axes.right.x;
        },
      },
    },
  },
  activate: function() {
    Object.keys(bind).forEach(function(btn_ax, i) {  //goes through btn or ax
      if(btn_ax != "activate") {
        Object.keys(bind[btn_ax]).forEach(function(piece, j) { //goes through buttons or left and right axes
          Object.keys(bind[btn_ax][piece]).forEach(function(which, k) {  //goes through the individual functions
            console.log(btn_ax+": "+piece+", "+which);
            gp[btn_ax+"_bind"](piece, which, bind[btn_ax][piece][which].func);
          });
        });
      }
    });
  }
}