from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import threading

from rov.rov import ROV

"""
PRIMARY FLASK APPLICATION:

This file handles the primary functions of the webapp. Handles:
    Routing
    SocketIO
        Error Handling
    Flask Init
"""

# GLOBALS:
app = Flask(__name__, static_url_path="", static_folder="frontend")
socketio = SocketIO(app, async_mode=None)

rov = ROV()


# ROUTING:
@app.route('/')
def index():
    print "Send index.html"
    return app.send_static_file('index.html')

@app.route('/UI/')
def index_front():
    print "Send /src/index.html"
    return app.send_static_file('src/index.html')

@app.route('/UI/<path:path>')
def send_UI_files(path):
    print path
    return send_from_directory('frontend/src/', path)

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

    # TODO:
    # Once this has been certified to work, the dictionary will be
    # created only once and then updated with new values in this method.

    return rov.data


if __name__ == '__main__':
    rov_run = threading.Thread(target=rov.run)
    rov_run.daemon = True
    rov_run.start()

    socketio.run(app, debug=True, host="0.0.0.0")
