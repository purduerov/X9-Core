<template>
	<div>
		<div class="wrapper">
			<h1>Save current settings:</h1>
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
    font-weight: 50;
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
    margin: 2px;
    box-sizing: border-box;
    outline: none;
    border: none;
    border-radius: 5px;
    font-size: 14px;
    min-height: 30px;
		width: 75%;
}

ul {
		font-size: 16px;
}
</style>
