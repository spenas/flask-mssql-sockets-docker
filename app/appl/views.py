import os
from flask import current_app as app
from flask import request, redirect,url_for


@app.route("/")
@app.route("/list")
def lists ():
	#Display the all Tasks
	todos_l = todos.find()
	a1="active"
	return 200

