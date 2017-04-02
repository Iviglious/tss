from app import app
from flask import render_template, request, jsonify
import unirest
from forms import MessageForm, ExpenseForm


@app.route('/')
@app.route('/index/')
def index():
	return render_template("index.html")


@app.route('/register/')
@app.route('/login/')
def todo():
	return render_template("todo.html")
