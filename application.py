from flask import Flask, send_from_directory, render_template
from flask_socketio import SocketIO
import threading
import os
import json

from rov.rov import ROV


import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
"""
PRIMARY FLASK APPLICATION:
This file handles the primary functions of the webapp. Handles:
    Routing
    SocketIO
        Error Handling
    Flask Init
"""

# GLOBALS:
<<<<<<< HEAD
app = Flask(__name__, static_url_path="", static_folder="frontend/src")
socketio = SocketIO(app, async_mode='eventlet')

rov = ROV()

last_rov = ""


# ROUTING:
@app.route('/')
def index():
    return app.send_static_file('index.html')

# SOCKET-IO:
@socketio.on('dearflask')
def recieve_controls(data):
    global last_controller, last_rov
    print data[-1:]
    # print data
    # parse json controls object into onside object.
    # print("controls: " + str(json))
    # print('received message: ' + str(data))
    #thruster set calc and pwm


    send_packet()

    if data != last_rov:
        on = [0, 0, 0, 0, 0, 0]
        ind = 0
        rov._data["dearflask"] = json.loads(data)
        for t, thrust in rov._data["dearflask"].thrusters:
            ind = int(t[-1:])
            on[ind] = thrust.active

        print rov.mapper.generate_thrust_map(on, rov._data["dearflask"].force)
        last_rov = data
        # print rov._data
        # print data


@socketio.on('connect')
def on_connect():
    print("CLIENT CONNECTED!")


@socketio.on('disconnect')
def on_disconnect():
    print("CLIENT DISCONNECTED!")


"""
# Error Handling (We should probably do something with this at some point..)
@socketio.on_error()
def error_handler(e):
    print(e)
    print("ERROR CAUGHT BY HANDLER!\n")
"""

# HELPER METHODS:

def send_packet():

    packet = build_dearclient()

    #print "Sent:"
    #print packet

    socketio.emit("dearclient", packet, json=True)

def build_dearclient():

    return rov.data()["dearclient"]

# def start_sio():
    #socketio.run(app, host="127.0.0.1")


if __name__ == 'application':
    #rov_run = threading.Thread(target=rov.run)
    #rov_run.daemon = True
    #rov_run.start()

    # socket_run = threading.Thread(target=start_sio)
    # socket_run.daemon = True
    # socket_run.start()

    socketio.run(app, use_reloader=False, debug=True, host="0.0.0.0")
