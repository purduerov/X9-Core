const electron = require('electron')
// Module to control application life.
const app = electron.app
// Module to create native browser window.
const BrowserWindow = electron.BrowserWindow

const path = require('path')
const url = require('url')

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
    mainWindow.setFullScreen(true)
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', app.quit)