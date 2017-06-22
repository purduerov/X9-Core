const electron = require('electron')
// Module to control application life.
const app = electron.app
// Module to create native browser window.
const BrowserWindow = electron.BrowserWindow

const path = require('path')
const url = require('url')

const fs = require('fs')
const ipc = electron.ipcMain

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow

function createWindow () {
    // Create the browser window.
    mainWindow = new BrowserWindow({
        // If you have a big enough monitor, use width: 2576 and height 1119
        // to make the display area match that of the ROV monitor. These are
        // Window's 10 specific to the titlebar and window outline widths.
        width: 1000,
        height: 800
    })

    // and load the index.html of the app.
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'src/index.html'),
        protocol: 'file:',
        slashes: true
    }))


/***************
    This is for saving and retrieving settings
    Here, all communication should be in string form;
    The webpage handles the Object-to-String conversion,
    for uniformity.
**************/

/*
//this was a test, writes a file with content typed in the window
ipc.on('PRINTMENOW', function(event, save) {
  //console.log(save);
  fs.writeFile('./settings/iwroteit.wut', save, function(err) {
    if(err) {
      throw err;
    }
  });
});
*/

//makes the settings file if it doesn't already exist
//GitHub should make this mute, but helps operations occur error-free.
    fs.access("./settings/", function(err) {
      if(err && err.code == 'ENOENT') {
        fs.mkdir("./settings/");
        console.log("Settings file created.");
      } else {
        console.log("Settings file exists.");
      }
      return;
    });

    ipc.on('listings', function(event) {

      var names = Object;
      fs.readdir('./settings/', function(err, files) {
        if(err) {
          throw err;
        } else {
/*          names = files.reduce(function(acc, cur, i) {
            acc[i] = cur;
            return acc;
          }, {});

*/
          console.log(files);
          event.sender.send('list-reply', files);
        }
      });
    });

    ipc.on('write', function(event, filename, save) {
      var bad = Boolean;
      fs.writeFile('./settings/'+filename, save, function(err) {
          if(err) {
            bad = true;
            throw err;
          } else {
            bad = false;
          }
        });

        console.log(bad==true);
        event.sender.send('write-reply', bad);
    });

    ipc.on('read', function(event, filename) {
      fs.readFile("./settings/"+filename, 'utf8', function(err, data) {
        if(err) {
          throw err;
        } else {
          event.sender.send('read-reply', data);
        }
      });

    });

    ipc.on('delete', function(event, filename) {
      var bad = Boolean;
      fs.unlink("./settings/"+filename, function(err) {
        if(err) {
          bad = true;
          throw err;
        } else {
          bad = false;
        }
      });

      event.sender.send('delete-reply', bad);
    });

    // Emitted when the window is closed.
    mainWindow.on('closed', function () {
        // Dereference the window object, usually you would store windows
        // in an array if your app supports multi windows, this is the time
        // when you should delete the corresponding element.
        mainWindow = null
    })

    // Maximize first, so that when coming out of full screen the window
    // is fully maximized.
    mainWindow.maximize()
    mainWindow.setFullScreen(false)
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', app.quit)
