const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'), // Подключим preload.js для безопасности
      nodeIntegration: true, // Включаем интеграцию Node.js для доступа к python-shell
      contextIsolation: false,
    },
  });

  win.loadFile('index.html');
  win.removeMenu();
}

app.on('ready', createWindow);
