import os
from flask import Flask, send_from_directory
from getsome import AppConfig
from getsome.core.main import serve_link

app = Flask(__name__, static_folder=AppConfig.server_www_files)

@app.route('/getsome')
def getsomeUrl():
    return serve_link()

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


def main():
    app.run(use_reloader=True, port=5000, threaded=True)

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)