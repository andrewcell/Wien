from flask import Flask

import psutil
import platform
import json

app = Flask(__name__)

def getWarning():
    if psutil.cpu_percent() >= 70.0 or psutil.virtual_memory().percent >= 85.0:
        return "Warning"

    else:
        return "Clear"

if platform.system() == 'Linux':
    information = {
        'status': getWarning(),
        'serverType': platform.system(),
        'serverVersion': platform.release(),
        'Distribution': platform.linux_distribution()
    }
else:
    information = {
        'status': getWarning(),
        'serverType': platform.system(),
        'serverVersion': platform.release(),
        'Distribution': ""
}

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/status')
def status():
    return json.dumps(information)

if __name__ == '__main__':
    app.run()
