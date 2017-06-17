<template>
<div>
	<div class="wrapper">
		<h1>Timer</h1>
		<br>
		<h1 id="timer"><span id="min">00</span>:<span id="seconds">00</span></h1>
		<br> <br>
		<div class="buttons">
			<button v-on:click="start()">Start</button>
			<button v-on:click="stop()">Stop</button>
			<button v-on:click="reset()">Reset</button>
		</div>
</div>
</div>
</template>

<script>

export default {
	mounted: function() {
		var tmr_ref = -1;
		var comp;

		var min_span = document.getElementById("min");
		var sec_span = document.getElementById("seconds");

		var that = this;

		console.log(that);
        
        /*
         *  Throws an extra zero in front of single digits.
         */
		this.time_string = function(num) {
			if(num < 10) {
				return "0"+num.toString();
            } else {
				return num.toString();
			}
		}

		this.start = function() {
			if(tmr_ref == -1) {
				if(sec_span == null) {		//initial initialization returning null...
					min_span = document.getElementById("min");
					sec_span = document.getElementById("seconds");
				}
				console.log(document.getElementById("min"));

				var s_cur = parseInt( sec_span.textContent );
				var m_cur = parseInt( min_span.textContent );
				comp = Date.now() - ((m_cur*60)+s_cur)*1000;		//this is in milliseconds
				var blip;

				var sec;
				var min;

				tmr_ref = setInterval(function() {
					blip = parseInt((Date.now() - comp)/1000);		//this is in seconds

					min = parseInt(blip / 60);
					console.log(blip+"\n"+(blip / 60)+"\n"+min);
					sec = blip % 60;

					sec_span.textContent = that.time_string(sec);
					min_span.textContent = that.time_string(min);
                    if (min == 14 && sec == 58)
                        setInterval(function() {
                                var timer = document.getElementById("timer");
                                if (timer.style.color == "red") 
                                    timer.style.color = "white";
                                else
                                    timer.style.color = "red";
                        }, 2000);

				}, 10);
			}
		}

		this.stop = function() {
			if(sec_span == null) {		//initial initialization returning null...
				sec_span = document.getElementById("min");
				ten_span = document.getElementById("seconds");
			}
			console.log(document.getElementById("min"));
			if(tmr_ref != -1) {
				clearInterval(tmr_ref);
				tmr_ref = -1;
				comp = -5;
			} else {
				console.log("Extra stop press.");
			}
		}

		this.reset = function() {
			if(sec_span == null) {		//initial initialization returning null...
				sec_span = document.getElementById("min");
				ten_span = document.getElementById("seconds");
			}
			if(tmr_ref != -1) {
				clearInterval(tmr_ref);
				tmr_ref = -1;
				comp = -5;
			}

			sec_span.textContent = "00";
			min_span.textContent = "00";
		}

		this.reset();
	}
}

</script>

<style scoped>
h1 {
    font-weight: 400;
}


.left {
    display: flex;
    width: 50%;
    height: 100%;
    flex-direction: column;
}

.right {
    display: flex;
    width: 50%;
    height: 100%;
    flex-direction: column;
}

.trst {
    display: flex;
    flex-direction: row;
}

.buttons{
    position: absolute;
    width: 400px;
    height: 50px;
    display: flex;
    justify-content: space-between;
    color: black;
}

</style>
