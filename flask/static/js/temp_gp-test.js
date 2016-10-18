var active_div = function() {
  var div = $("#moving");
  var info = $("#info");
  var txt = "";
  if(gp.buttons.a.press && !gp.buttons.b.press) {
      div.css("background-color", "cyan");
  } else if(gp.buttons.b.press && !gp.buttons.a.press) {
      div.css("background-color", "red");
  }

  if(gp.buttons.y.press && !gp.buttons.x.press) {
      div.height("+=2");
      div.width("+=2");
      div.css({top: "-=1px"});
      div.css({left: "-=1px"});
  } else if(gp.buttons.x.press && !gp.buttons.y.press) {
      div.height("-=2");
      div.width("-=2");
      if(div.width() != 0) {
          div.css({top: "+=1px"});
          div.css({left: "+=1px"});
      }
  }

  div.css({top: "+="+parseInt(10*gp.axes.yleft.pos)+"px"});
  div.css({left: "+="+parseInt(10*gp.axes.xleft.pos)+"px"});
  
  
  Object.keys(gp.buttons) .forEach(function(key_b, i) {
    if(key_b != "length"){
      txt = txt+"</br>"+key_b+": "+gp.buttons[key_b].press;
      //console.log("Buttons: "+gp.buttons[key_b].pressed+" "+key_b);
    }
  });
  Object.keys(gp.axes).forEach(function(key_a, i) {
    if(key_a != "length"){
        if(key_a.substring(0,1) == "y") {
        //txt = txt+"</br>"+key_a+": "+parseInt(-10*gp.axes[key_a].pos);
        txt = txt+"</br>"+key_a+": "+(-gp.axes[key_a].pos);
        //console.log("Axes: "+gp.axes[key_a]+" "+key_a);
        } else {
        //txt = txt+"</br>"+key_a+": "+parseInt(10*gp.axes[key_a].pos);
        txt = txt+"</br>"+key_a+": "+gp.axes[key_a].pos;
        //console.log("Axes: "+gp.axes[key_a]+" "+key_a);
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
    var ab
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
});