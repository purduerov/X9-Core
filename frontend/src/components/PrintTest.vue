<template>
<div>
	<div class="wrapper">
		<h1>Timer</h1>
		<br>
		<br>Save me to file:<br>
    <input id="savin" type="text"></input>
		<div class="buttons">
			<button v-on:click="print()">Print me away! A secret place! A sweet escape!</button>
		</div>
</div>
</div>
</template>

<script>

  export default {
  	mounted: function() {
      const {shell, app, ipcRenderer} = window.require('electron');
      const el = document.getElementById("savin");

      this.print = function() {
        var wurdz = el.value;
        ipcRenderer.send('PRINTMENOW', wurdz);
        //console.log(wurdz);
      }
    }
  }

</script>

<style scoped>
h1 {
    font-weight: 400;
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
