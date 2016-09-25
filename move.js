$(document).ready(function() {
	var gp = navigator.getGamepads();
	var div = $("#moving");
	var mes = $("#messages");
	mes.text(Object.getOwnPropertyNames(gp));

	//while(1) {
		gp = navigator.getGamepads();
		if(gp != null && gp != undefined) {
			div.text("good");
			gp.a = gp[0].buttons[0].pressed;
			gp.b = gp[0].buttons[1].pressed;
			gp.x_ax = gp[0].axes[0];
			gp.y_ax = gp[0].axes[1];

			if(gp.a && !gp.b) {
				div.css("background-color", "cyan");
			} else if(gp.b && !gp.a) {
				div.css("background-color", "red");
			}
			
			
			div.css({top: "+="+(10*gp.y_ax).toFixed(0)+"px"});
			div.css({left: "+="+(10*gp.x_ax).toFixed(0)+"px"});
		} else {
			div.text("bad");
			mes.append("\n"+(gp == null)+"\n"+(gp == undefined));
		}
	//}
});
