import os
from flask import current_app as app
from flask import render_template, request, redirect,url_for


@app.route("/")
@app.route("/list")
def lists ():
	#Display the all Tasks
	todos_l = todos.find()
	a1="active"
	return render_template('index.html',a1=a1,todos=todos_l,t=title,h=heading)

