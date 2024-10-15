const { PythonShell } = require('python-shell');
const path = require('path');

function installForge() {
    const version = document.getElementById('version').value;
    if (!version) {
        document.getElementById('output').innerText = 'Please enter a version.';
        return;
    }

    let options = {
        scriptPath: path.join(__dirname, '/'), // Путь к Python скрипту
        args: [version] // Передаем версию как аргумент
    };

    PythonShell.run('main.py', options, function (err, results) {
        if (err) {
            document.getElementById('output').innerText = 'Error: ' + err;
            return;
        }
        document.getElementById('output').innerText = results.join('\n');
    });
}

function launchGame() {
    const version = document.getElementById('version').value;
    const username = document.getElementById('username').value || 'Player';

    if (!version) {
        document.getElementById('output').innerText = 'Please enter a version.';
        return;
    }

    console.log(`Launching game with version: ${version}, username: ${username}`); // Лог в консоль

    let options = {
        scriptPath: path.join(__dirname, '/'), // Путь к Python-скрипту
        args: ['launch', version, username],  // Передаем команду, версию и имя
        pythonPath: 'python3',  // Убедитесь, что это путь к вашей версии Python
    };

    PythonShell.run('main.py', options, function (err, results) {
        if (err) {
            console.error('Python error:', err);  // Выводим ошибку в консоль
            document.getElementById('output').innerText = 'Error: ' + err.message;
            return;
        }
        console.log('Python output:', results);  // Логируем результат
        document.getElementById('output').innerText = results.join('\n');
    });
}


function getInstalledVersions() {
    let options = {
        scriptPath: path.join(__dirname, '/'), // Путь к Python скрипту
        args: ['get_versions'] // Команда для получения версий
    };

    PythonShell.run('main.py', options, function (err, results) {
        if (err) {
            document.getElementById('output').innerText = 'Error: ' + err;
            return;
        }
        document.getElementById('output').innerText = 'Installed Versions:\n' + results.join('\n');
    });
}
