from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from flask_socketio import SocketIO
import os
import socketio as sio

socketio = SocketIO()
sio = sio.Client()

def create_app():
    #initialize the app
    app = Flask(__name__, instance_relative_config=False)
    #initialize plugins
    socketio.init_app(app = app)
    sio.connect('http://localhost:4000')

    with app.app_context():
        # from .socket_client import socket_client
        from . import views
        # app.register_blueprint(socket_client)

        return app
