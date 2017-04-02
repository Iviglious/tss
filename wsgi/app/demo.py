from app import app
from flask import render_template, request, jsonify
import unirest
from forms import MessageForm, ExpenseForm
import DB

# normal opening of the demo page
@app.route('/demo/')
def demo():
	# read from db to get all expenses and visualise them
	all_expenses = DB.get_all_expenses()

	html = render_template("demo.html", form=ExpenseForm(), expenses=all_expenses, message=None)
	return html

# opening of the demo page with POST method - adding an expense
@app.route('/demo/', methods=['POST'])
def demo_post():
	user_name = request.form['user_name']
	expense_date = request.form['expense_date']
	expense_amount = request.form['expense_amount']
	expense_description = request.form['expense_description']

	msg = None
	if user_name: # it's a request to add a new expense
		msg = DB.add_expense(user_name, expense_date, expense_amount, expense_description)
	
	# read from db to get all expenses and visualise them
	all_expenses = DB.get_all_expenses()

	html = render_template("demo.html", form=ExpenseForm(), expenses=all_expenses, message=msg)
	return html
