function settings() {
    const {shell, app, ipcRenderer} = window.require('electron');
    const el = document.getElementById("save_new");

    var selected = undefined;
    var title = $("#save_new");
    var message = $("#set_mess");
    var asets = $(".asetting");
    var setlist = $("#set_list");


    /*********
        Updates the list to reflect what's in the filesystem.
        Assumes newlist is accurate against the filesystem, and an Array.
    *********/
    var settingUpdate = function(newlist) {

        vue.config.list.forEach(function(curVal, i) {
            if(-1 == $.inArray(curVal, newlist) ) {
                $("#"+curVal).remove();   //splicing with this makes this function miss multiple
            }                             //user-deleted files
        });

        newlist.forEach(function(curVal, i) {
            if(-1 == $.inArray(curVal, vue.config.list) ) {
                setlist.append("<li class=\"asetting\" id=\""+curVal+"\">"+curVal+"<li>");

                let item = $("#"+curVal);
                item.click(function() {
                    selected = item;
                    console.log(selected);
                    asets.css("color", "white");
                    item.css("color", "cyan");
                });
            }
        });

        asets = $(".asetting");   //gotta refresh the list, so new elements are effected

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
            let data = {};

            Object.keys(vue.config).forEach(function(cur, i) {
                if(cur != "list") {
                    data[cur] = vue.config[cur];
                }
            });

            ipcRenderer.send('write', name, JSON.stringify(data) );
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
          selected.css("color", "white");
        }
    });

    $("#del").click(function() {
        console.log("Deleting");
        if(selected != undefined) {
            ipcRenderer.send('delete', selected.text() );
            console.log("Here");
            selected.remove();   //this is throwing an error, 'b.replace is not a function'
            console.log("No, here");
        } else {
          console.log("Selected is undefined.");
        }
    });

    $("#refresh").click(function() {
        console.log("Refreshing");
        ipcRenderer.send('listings');
    });

    /**********
        This is where the webpage listens for Electron to respond to a call.
    **********/

    ipcRenderer.on('write-reply', function(event, bad) {
        console.log(bad == true);
        if(bad) {
            message.text("Failed to save properly");
        } else {
            console.log("Refreshing");
            ipcRenderer.send('listings');
        }
    });

    ipcRenderer.on('delete-reply', function(event, bad) {
        if(bad) {
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
      console.log(scaling);
        window.play = scaling;
        var scales = JSON.parse(scaling);

        Object.keys(scales).forEach(function(key, i) {
          vue.config[key] = scales[key];
        });
    });

    vue.config.list = [];
    ipcRenderer.send('listings');
}

module.exports = settings
