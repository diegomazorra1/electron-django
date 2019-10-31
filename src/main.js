// Modules to control application life and create native browser window
import {app, BrowserWindow} from 'electron'
import path from 'path'
import devtools from './devtools'


if (process.env.NODE_ENV == 'development') {
  devtools()

}
// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.

let mainWindow

function createWindow () {
  // Create the browser window.
// var subpy = require('child_process').spawn('dist/proyecto_ejemplo/proyecto_ejemplo.exe', ['runserver']);
  var subpy = require('child_process').spawn('python', ['manage.py', 'runserver']);
//  var subpy = require('child_process').spawn('python', ['./manage.py', 'fruffnserver']);

    var rq = require('request-promise');
    var mainAddr = 'http://localhost:8000/';
    var openWindow = function() {
        mainWindow = new BrowserWindow({ width: 800, height: 600 })
        mainWindow.loadURL('http://localhost:8000');

        mainWindow.on('closed', function() {
            mainWindow = null;
            subpy.kill('SIGINT');

        //
        //    var subpy2 = require('child_process').spawn('TASKKILL', ['/F', '/IM', 'python.exe', '/T']);


        })
    }

    var startUp = function() {
        rq(mainAddr)
            .then(function(htmlString) {
                console.log('Django iniciado!');
                openWindow();
            })
            .catch(function(err) {
                startUp();
            });
    };
    startUp();


  // Open the DevTools.
  // mainWindow.webContents.openDevTools()

  // Emitted when the window is closed.

}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', function () {

  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin')
  //console.log('Saliendo....')

  app.quit()

})

app.on('before-quit', function() {
//  subpy.kill('SIGINT')
//  subpy.removeAllListeners('close')
//  mainWindow = null
//  subpy.kill('SIGINT')
  console.log('Saliendo..')


})

app.on('activate', function () {
//  win.toggleDevTools();
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
   if (mainWindow === null) createWindow()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
