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
app = Flask(__name__) #static_url_path="", static_folder="frontend/src")
socketio = SocketIO(app, async_mode='eventlet')

rov = ROV()

last_rov = {}


# ROUTING:
@app.route('/')
def index():
    print "Send index2.html"
    return send_from_directory('frontend/src/', 'index2.html')

@app.route('/fonts/<path:path>')
def send_font_files(path):
#    print "front file"
#    print path
    return send_from_directory('frontend/src/', path)

@app.route('/gp/<path:path>')
def send_UI_files(path):
#    print "UI file"
#    print path
#    print os.path.dirname(os.path.realpath(__file__))
    return send_from_directory('frontend/gamepad/', path)

@app.route('/pg2/<path:path>')
def send_index2_page_files(path):
#    print "Page file"
#    print path
    return send_from_directory('frontend/src/', path)

# SOCKET-IO:
@socketio.on('dearflask')
def recieve_controls(data):
    global last_controller, last_rov
    print data
    # parse json controls object into onside object.
    # print("controls: " + str(json))
    # print('received message: ' + str(data))
    send_packet()
    
    if data != last_rov:
        last_rov = data
        rov._data["dearflask"] = json.loads(data)
        print rov._data
        print data


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
