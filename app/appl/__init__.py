from flask import Flask, render_template,request,redirect,url_for # For flask implementation
import os

def create_app():
    #initialize the app
    app = Flask(__name__, instance_relative_config=False)
    #initialize plugins


    with app.app_context():
        from . import views

        return app