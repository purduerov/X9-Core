const electron = require('electron')
// Module to control application life.
const app = electron.app
// Module to create native browser window.
const BrowserWindow = electron.BrowserWindow

const path = require('path')
const url = require('url')

//const fs = require('fs')
//const ipc = require('ipc')

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow
let viewWindow

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

    viewWindow = new BrowserWindow({
        //this window is meant to be used with the large monitor
        //change these values to 2576 & 1119 once it's hooked up
        width: 1000,
        height: 800
    })

    viewWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'src2/index2.html'),
        protocol: 'file:',
        slashes: true
    }))
/*
    fs.access("./settings/", function(err) {
      if(err && err.code == 'ENOENT') {
        fs.mkdir("./settings/");
      }
      return;
    });

    ipc.on('listings', function () {
      var names = Array;
      fs.readdir('./settings/', function(err, files) {
        if(err) {
          throw err;
        } else {
          names = files;
        }
        return;
      });

      return names;
    });

    ipc.on('write', function(filename, save) {
      fs.writeFile('./settings/'+filename, save, function(err) {
        if(err) {
          throw err;
        }
      });
    });

    ipc.on('read', function(filename, copy) {
      var content = String;
      fs.readFile(filename, function(err, data) {
        if(err) {
          throw err;
        } else {
          content = data;
        }
        return;
      });

      return content;
    });

    ipc.on('delete', function(filename) {
      fs.unlink(filename, function(err) {
        if(err) {
          throw err;
        }
      });
    });
*/
    // Emitted when the window is closed.
    mainWindow.on('closed', function () {
        // Dereference the window object, usually you would store windows
        // in an array if your app supports multi windows, this is the time
        // when you should delete the corresponding element.
        mainWindow = null
    })

    viewWindow.on('closed', function () {
      viewWindow = null
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
