from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
#import json parser

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
app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)


# Statistics:
recieve_count = 0  # keeps count of how many json objects flask has recieved.
send_count = 0 # keeps count of how many json objects flask has sent.



# ROUTING:

@app.route('/')
def index():
    return render_template(url_for('static', filename='index.html', async_mode=socketio.async_mode))



# SOCKET-IO:

@socketio.on('dearflask')
def recieve_controls(json):
    # parse json controls object into onside object.
    print("controls: " + str(json))
    recieve_count += 1

@socketio.on('dearclient')
def send_packet():
    json = "{ empty }"
    print("sent: " + str(json))
    socketio.send(json, json=True)
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
