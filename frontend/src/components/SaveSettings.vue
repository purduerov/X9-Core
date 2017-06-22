<template>
	<div>
		<div class="wrapper">
			<br>Save current settings:<br>
	    <input id="save_new"></input>
			<div class="buttons">
				<button id="save">Save</button>
				<button id="read">Load</button>
				<button id="del">Delete</button>
				<button id="refresh">Refresh</button>
			</div>
			<p id="set_mess"><p>
      <h1>Settings:</h1>
      <hr>
      <ul id="set_list"></ul>

		</div>
	</div>
</template>

<script>
  export default {
		props: ['data'],
  }

</script>

<style scoped>
h1 {
    font-weight: 400;
}

.buttons{
    position: static;
    width: 400px;
    height: 50px;
    display: flex;
		padding: 5px;
    color: black;
}

#set_mess {
		height: 25px;
		width: 100%;
}

input {
		border-radius: 5px;
}
</style>
