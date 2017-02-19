var active_div = function() {
  var div = $("#moving");
  var info = $("#info");
  var txt = "";
  if(gp.buttons.a.val && !gp.buttons.b.val) {
      div.css("background-color", "cyan");
  } else if(gp.buttons.b.val && !gp.buttons.a.val) {
      div.css("background-color", "red");
  }

  if(gp.buttons.y.val && !gp.buttons.x.val) {
      div.height("+=2");
      div.width("+=2");
      div.css({top: "-=1"});
      div.css({left: "-=1"});
  } else if(gp.buttons.x.val && !gp.buttons.y.val) {
      div.height("-=2");
      div.width("-=2");
      if(parseInt(div.width()) != 0) {
          div.css({top: "+=1"});
          div.css({left: "+=1"});
      }
  }

  if(gp.buttons.up.pressed) {
    div.css({top: "0"});
  }
  if(gp.buttons.down.released) {
    div.css({top: "100%"});
    div.css({top: "-="+(div.height()+3)});
  }
  if(gp.buttons.left.pressed) {
    div.css({left: "0"});
  }
  if(gp.buttons.right.released) {
    div.css({left: "100%"});
    div.css({left: "-="+(div.width()+3)});
  }



  div.css({top: "+="+parseInt(-10*gp.axes.left.y)+"px"});
  div.css({left: "+="+parseInt(10*gp.axes.left.x)+"px"});


  Object.keys(gp.buttons) .forEach(function(key_b, i) {
    if(key_b != "length"){
      txt = txt+"</br>"+key_b+": "+(!!+gp.buttons[key_b].val);
      //console.log("Buttons: "+gp.buttons[key_b].val+" "+key_b);
    }
  });
  Object.keys(gp.axes).forEach(function(key_a, i) {
    if(key_a != "length"){
        txt = txt+"</br>"+key_a+"</br><p>  x: "+(gp.axes[key_a].x)+"</br>  y: "+(gp.axes[key_a].y)
                 +"</br>  &theta;: "+gp.axes[key_a].theta+"</br>  r: "+gp.axes[key_a].r+"</p>";
        //console.log("Axes: "+gp.axes[key_a]+" "+key_a);
        if(key_a == "right") {
/*          txt = txt + "</br></br> x - x-off: " + (navigator.getGamepads()[gp.i_use].axes[layouts[gp.layout].axes[key_a].x])
                    + "</br> 1 - x-off: " + (1 - gp.getDisplace().right.x);
*/
        }
      }
  });

  info.html(txt);
}

var go1 = -1;
var go2 = -1;

var run = function(abt) {
  if(gp.ready) {
    window.clearInterval(go1);
    go1 = -1;
    go2 = window.setInterval(function() {
      gp.get_current(abt);
      if(gp.ready) {
        active_div();
      } else {
        $("#reset").click();
      }
    }, 10);
  }
}

$(document).ready(function() {
  var abt = $("#titles");
  gp.set(abt);

  go1 = window.setInterval(function() { run(abt); }, 50);

  $("#reset").click(function() {
    if(go2 != -1) {
      gp.ready = false;
      window.clearInterval(go2);
    } else {console.log("go2: "+go2+" go1: "+go1);}
    $("#info").empty();
    gp.set(abt);
    go1 = window.setInterval(function() { run(abt); }, 50);
  });

  $("#bind").click(function() {
    gp.bind("a", "press", function(arg) { arg.message.html("Re-link, </br>\'"+arg.btn+"\' says hi "+arg.count+" times!"); arg.count += 1; },
            {message: $("#reset"), btn: "a", count: 0});
  });
});
