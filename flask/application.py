from flask import Flask, render_template
from flask import url_for
from flask_socketio import SocketIO, send, emit
# import json parser

#
# PRIMARY FLASK APPLICATION:
#
# This file handles the primary functions of the webapp. Handles:
#   Routing
#   SocketIO
#       Error Handling
#   Flask Init


# GLOBALS:
async_mode = None
app = Flask(__name__, static_folder="static")
socketio = SocketIO(app, async_mode=async_mode)


# Statistics:
recieve_count = 0  # keeps count of how many json objects flask has recieved.
send_count = 0  # keeps count of how many json objects flask has sent.


# ROUTING:

@app.route('/')
def index():
    return render_template('index.html')

# SOCKET-IO:


@socketio.on('dearflask')
def recieve_controls(json):
    # parse json controls object into onside object.
    #print("controls: " + str(json))
    global recieve_count
    recieve_count += 1
    print(recieve_count)
    print('received message: ' + str(json))


@socketio.on('dearclient')
def send_packet():
    json = {"text": "Hello World"}

    print("sent: " + str(json))

    socketio.emit("response", json, json=True)

    global send_count
    send_count += 1


@socketio.on('connect')
def on_connect():
    print("CLIENT CONNECTED!")



@socketio.on('disconnect')
def on_disconnect():
    print("CLIENT DISCONNECTED!")

# Error Handling


@socketio.on_error()
def error_handler(e):
    print("ERROR CAUGHT BY HANDLER!\n")

# INIT:
if __name__ == '__main__':
    socketio.run(app, debug=True)
