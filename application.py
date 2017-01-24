from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import threading
import os
from cam import Camera

"""
PRIMARY FLASK APPLICATION:

This file handles the primary functions of the webapp. Handles:
    Routing
    SocketIO
        Error Handling
    Flask Init
"""

# GLOBALS:
app = Flask(__name__, static_url_path="", static_folder="")
socketio = SocketIO(app, async_mode=None)

camera1 = Camera()
camera2 = Camera(device='/dev/video1', port=8081)
camera3 = Camera(device='/dev/video2', port=8082)
camera1.on()
camera2.on()
camera3.on()


# ROUTING:
@app.route('/')
def index():
    print "Send webpage.html"
    return app.send_static_file('webpage.html')

@app.route('/UI/')
def index_front():
    print "Send /src/index2.html"
    return app.send_static_file('src/index2.html')

@app.route('/UI/fonts/<path:path>')
def send_font_files(path):
    print "front file"
    print path
    return send_from_directory('frontend/src/', path)

@app.route('/UI/gp/<path:path>')
def send_UI_files(path):
#    print "UI file"
#    print path
    print os.path.dirname(os.path.realpath(__file__))
    return send_from_directory('frontend/gamepad/', path)

@app.route('/UI/pg2/<path:path>')
def send_index2_page_files(path):
    print "Page file"
    print path
    return app.send_static_file('src/'+path)

# SOCKET-IO:
@socketio.on('dearflask')
def recieve_controls(data):
    # parse json controls object into onside object.
    # print("controls: " + str(json))
    print('received message: ' + str(data))


@socketio.on('dearclient')
def send_packet():

    packet = build_dearclient()

    #print "Sent:"
    #print packet

    socketio.emit("dearflask", packet, json=True)


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


def build_dearclient():

    return rov.data


if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")
