<template>
<div>
	<div class="wrapper">
		<h1>Timer</h1>
		<br>
		<h1><span id="seconds">00</span>:<span id="tens">00</span></h1>
		<br> <br>
		<div class="buttons">
			<button id="button-start">Start</button>
			<button id="button-stop">Stop</button>
			<button id="button-reset">Reset</button>
		</div>	
</div> 
</div>
</template>

<script>
	window.onload = function () {
  
  var seconds = 0; 
  var tens = 0; 
  var appendTens = document.getElementById("tens")
  var appendSeconds = document.getElementById("seconds")
  var buttonStart = document.getElementById('button-start');
  var buttonStop = document.getElementById('button-stop');
  var buttonReset = document.getElementById('button-reset');
  var Interval ;

  buttonStart.onclick = function() {
    
     clearInterval(Interval);
     Interval = setInterval(startTimer, 10);
  }
  
    buttonStop.onclick = function() {
       clearInterval(Interval);
  }
  

  buttonReset.onclick = function() {
     clearInterval(Interval);
    tens = "00";
  	seconds = "00";
    appendTens.innerHTML = tens;
  	appendSeconds.innerHTML = seconds;
  }
  
   
  
  function startTimer () {
    tens++; 
    
    if(tens < 9){
      appendTens.innerHTML = "0" + tens;
    }
    
    if (tens > 9){
      appendTens.innerHTML = tens;
      
    } 
    
    if (tens > 99) {
      console.log("seconds");
      seconds++;
      appendSeconds.innerHTML = "0" + seconds;
      tens = 0;
      appendTens.innerHTML = "0" + 0;
    }
    
    if (seconds > 9){
      appendSeconds.innerHTML = seconds;
    }
  
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
