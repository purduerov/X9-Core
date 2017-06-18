<template>
	<div>
		<div class="wrapper">
			<br>Save current settings:<br>
	    <input id="save_new" type="text"></input>
			<div class="buttons">
				<button v-on:click="save()">Save</button>
				<button v-on:click="read()">Load</button>
				<button v-on:click="del()">Delete</button>
				<button v-on:click="refresh()">Refresh</button>
			</div>

      <h1>Settings:</h1>
      <hr>
      <ul v-for="value in list">
          <li class="set">{{value}}</li>
          <hr>
      </ul>

		</div>
	</div>
</template>

<script>

  export default {
		props: ['data'],
  	mounted: function() {
      const {shell, app, ipcRenderer} = window.require('electron');
      const el = document.getElementById("save_new");
			var that = this;
			var sel;

			var list = Array;
			var cont = String;

/**********
		Here, the buttons make their calls to electron to work with files.
		Object <--> String conversions handled in the webpage, for uniformity.
**********/

			this.refresh = function() {
				ipcRenderer.send('listings'); //need to find how to receive feedback
			}

			//selects a file's list element for use in reading/deleting
			this.select = function(that) {
				sel = that;
			}

			//saves a file if named (research errors in name symbols later)
      this.save = function() {
        var wurdz = el.value;

				if(wurdz == "") {
					el.value = "Name your file!";
				} else if(wurdz != "Name your file!"){
					cont = JSON.stringify(that.data);
					console.log(cont);
					ipcRenderer.send('write', wurdz, cont);		//need to find how to receive feedback
				}
        //console.log(wurdz);
      }

			this.del = function() {
				//insert prompt here
				//if prompt says true, do:
				ipcRenderer.send('delete', sel.value);
			}

			this.read = function() {
				ipcRenderer.send('read', sel.value);	//need to find how to receive feedback
			}

/********
		This is where the webpage listens to electron
********/

			ipcRenderer.on('list-reply', function(event, files) {
				list = files;

				Object.keys(temp).forEach(function(key, i) {
					that.data[key] = temp[key];
				});
			});

			ipcRenderer.on('read-reply', function(event, scaling) {
				var temp = JSON.parse(scaling);
				console.log(scaling);
				console.log(temp);

				Object.keys(temp).forEach(function(key, i) {
					that.data[key] = temp[key];
				});
			});


    }
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

</style>
