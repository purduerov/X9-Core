
var hasGP = false;
var repGP;

function checkGaming() {
	return "getGamepads" in navigator;
}

function readGamepad(mes) {
    var div = $("#moving");
    var gp = navigator.getGamepads();

    gp = navigator.getGamepads();
    if(gp != undefined && gp != null) {
        var i = 0;
        while(gp[1] == undefined || gp[i].id != "Xbox 360 Controller (XInput STANDARD GAMEPAD)") {
            i++;
        }

        if(i < gp.length) {
            gp.a = gp[i].buttons[0].pressed;
            gp.b = gp[i].buttons[1].pressed;
            gp.x = gp[i].buttons[2].pressed;
            gp.y = gp[i].buttons[3].pressed;
            gp.x_ax = gp[i].axes[0];
            gp.y_ax = gp[i].axes[1];
            mes.text("A: "+gp.a+"    B: "+gp.b+"    X: "+gp.x+"    Y: "+gp.y+"\n"
                     +"X-axis: "+parseInt(gp.x_ax*10)+"    Y-axix: "+parseInt(gp.y_ax*-10));

            if(gp.a && !gp.b) {
                div.css("background-color", "cyan");
            } else if(gp.b && !gp.a) {
                div.css("background-color", "red");
            }

            if(gp.y && !gp.x) {
                div.height("+=2");
                div.width("+=2");
                div.css({top: "-=1px"});
                div.css({left: "-=1px"});
            } else if(gp.x && !gp.y) {
                div.height("-=2");
                div.width("-=2");
                if(div.width() != 0) {
                    div.css({top: "+=1px"});
                    div.css({left: "+=1px"});
                }
            }

            div.css({top: "+="+parseInt(10*gp.y_ax)+"px"});
            div.css({left: "+="+parseInt(10*gp.x_ax)+"px"});
        }
    }
}


$(document).ready(function() {
    var mes = $("#messages");
    

    if(checkGaming()) {
        var GPcheck;

        mes.text("Connect your xbox1 gamepad and press any button!");
        
        $(window).on("gamepadconnected", function() {
console.log("connection event");
            hasGP = true;
            repGP = window.setInterval(function() {readGamepad(mes); }, 10);
        });

        $(window).on("gamepaddisconnected", function() {
            console.log("disconnect event");
            mes.text("gamepad disconnected");
            window.clearInterval(repGP);
        });

        checkGP = window.setInterval(function() {
console.log("check event");
            if(navigator.getGamepads()[0]) {
                if(!hasGP) {
                    $(window).trigger("gamepadconnected");
                }
                window.clearInterval(checkGP);
            }
        }, 1);
    }
});
