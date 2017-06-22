
function settings() {
    const {shell, app, ipcRenderer} = window.require('electron');
    const el = document.getElementById("save_new");

    var selected = undefined;
    var title = $("#save_new");
    var message = $("#set_mess");
    var setlist = $("#set_list");

    var settingUpdate = function(newlist) {

        if(newlist.length > vue.config.list.length) {
            newlist.forEach(function(curVal, i) {
                if(-1 == $.inArray(curVal, vue.config.list) ) {
                    setlist.append("<li class=\"asetting\" id=\""+curVal+"\">"+curVal+"<li>");
                }
            });
        } else if(newlist.length < vue.config.list.length) {
            vue.config.list.forEach(function(curVal, i) {
                if(-1 == $.inArray(curVal, newlist) ) {
                    vue.config.list.splice(i, 1);
                    $("#"+curVal).remove();
                }
            });
        }

        vue.config.list = newlist;
    }

    /***********
        This is the filesaving processes, communicating and receiving from Electron.
        Immediately below is the call from the webpage to Electron.
        All object <--> string conversion is handled here for consistency.
    **********/

    $("#save").click(function() {
        console.log("Saving");
        var name = title.val();

        if(name === "" || name === "Name already used") {
            title.val("Please name your file");
        } else if(($.inArray(name, vue.config.list) + 1)) {
            title.val("Name already used");
        } else if(name != "Please name your file") {
            ipcRenderer.send('write', name, JSON.stringify(vue.config) );
        } else {
          console.log("Failed\n"+name);
        }
    });

    $("#read").click(function() {
        console.log("Reading");
        if(selected != undefined) {
            ipcRenderer.send('read', selected.text() );
        } else {
          console.log("Selected is undefined.");
        }
    });

    $("#del").click(function() {
        console.log("Deleting");
        if(selected != undefined) {
            ipcRenderer.send('delete', selected.text() );
            setlist.remove(selected);
        } else {
          console.log("Selected is undefined.");
        }
    });

    $("#refresh").click(function() {
        console.log("Refreshing");
        ipcRenderer.send('listings');
    });

    $(".asetting").click(function() {
        selected = this;
        console.log(selected.val() );
    });

    /**********
        This is where the webpage listens for Electron to respond to a call.
    **********/

    ipcRenderer.on('write-reply', function(bad) {
        console.log(bad == true);
        if(bad === true) {
            message.text("Failed to save properly");
        } else {
            console.log("Refreshing");
            ipcRenderer.send('listings');
        }
    });

    ipcRenderer.on('delete-reply', function(bad) {
        if(bad === true) {
            message.text("Failed to delete properly");
        } else {
            console.log("Refreshing");
            ipcRenderer.send('listings');
        }
    });

    ipcRenderer.on('list-reply', function(event, files) {
        settingUpdate(files);
    });

    ipcRenderer.on('read-reply', function(event, scaling) {
        var scales = JSON.parse(scaling);

        Object.keys(scales).forEach(function(key, i) {
          vue.config[key] = scales[key];
        });
    });

    vue.config.list = [];
    ipcRenderer.send('listings');
}

module.exports = settings
