#!/usr/bin/env python3
# File: chat_server.py
# Author: Blaine Winslow (CBW)
# Date: 2025-04-06
# Purpose: Run a local Flask chat room with real-time messaging over SocketIO

from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import logging

# --- Setup ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'cbw-secure-chat'
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')

# --- Routes ---
@app.route('/')
def index():
    return render_template('chat.html')

# --- Message Handler ---
@socketio.on('message')
def handleMessage(msg):
    print(f"[CHAT] {request.remote_addr}: {msg}")
    send(msg, broadcast=True)

# --- Main ---
if __name__ == '__main__':
    logging.getLogger('werkzeug').setLevel(logging.ERROR)  # Quiet logs
    print("Chat room live at http://<your-ip>:5000")
    socketio.run(app, host='0.0.0.0', port=5000)
