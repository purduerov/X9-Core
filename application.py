import json
import os
import threading

from flask import Flask, send_from_directory
from flask_socketio import SocketIO

from rov.rov import ROV


app = Flask(__name__, static_url_path="", static_folder="frontend/src")
socketio = SocketIO(app)

rov = ROV()

@app.route('/')
def index():
    return app.send_static_file('index.html')


@socketio.on('connect')
def on_connect():
    print("Client Connected!")


@socketio.on('disconnect')
def on_disconnect():
    print("Client Disconnected!")


@socketio.on('control-data')
def recieve_controls(data):
    rov.control_data = data


@socketio.on('ask-rov-data')
def ask_rov_data():
    socketio.emit('rov-data', rov.data, json=True)


if __name__ == 'application':
    rov_run = threading.Thread(target=rov.run)
    rov_run.daemon = True
    rov_run.start()
