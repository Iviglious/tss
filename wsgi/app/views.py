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


# normal opening of the demo page
@app.route('/demo/')
def demo():
	# read from db to get all expenses and visualise them
	all_expenses = get_all_expenses()

	return render_template("demo.html", form=ExpenseForm(), expenses=all_expenses, message=None)

# opening of the demo page with POST method - adding an expense
@app.route('/demo/', methods=['POST'])
def demo_post():
	user_name = request.form['user_name']
	expense_date = request.form['expense_date']
	expense_amount = request.form['expense_amount']
	expense_description = request.form['expense_description']

	msg = None
	if user_name: # it's a request to add a new expense
		msg = add_expense(user_name, expense_date, expense_amount, expense_description)
	
	# read from db to get all expenses and visualise them
	all_expenses = get_all_expenses()

	return render_template("demo.html", form=ExpenseForm(), expenses=all_expenses, message=msg)


@app.route('/api/1.0/expenses')
def get_expenses():
	expenses_arr =[
			 {'id':1, 'type':'Other','amount':1.34}
			,{'id':2, 'type':'Other','amount':5.10}
		]
	return jsonify({'expenses':expenses_arr})


@app.route('/emotion/')
def emotion():
	return render_template("my_form.html", mood='Question', form=MessageForm())

@app.route('/emotion/', methods=['POST'])
def emotion_post():
	msg = request.form['message']
	response = unirest.post("https://community-sentiment.p.mashape.com/text/",
		headers={
			"X-Mashape-Key": "6VWQcE5umumsh9oLsHfFlOseFGbDp1caaUKjsnj6PJRqxZKslv",
			"Content-Type": "application/x-www-form-urlencoded",
			"Accept": "application/json"
    			},
		params={
			"txt": msg
			}
	)
	return render_template("my_form.html",mood=response.body['result']['sentiment'],form=MessageForm())

# helping functions for the demo
def add_expense(user_name, expense_date, expense_amount, expense_description):
	return "Expense added successfully!"

def get_all_expenses():
	return [
		 {'user_name':'ivo', 'date':1, 'amount':1.34}
		,{'user_name':'ivo', 'date':2, 'amount':4.46}
		,{'user_name':'ivo', 'date':3, 'amount':6.30}
		,{'user_name':'aline', 'date':1, 'amount':1.64}
		,{'user_name':'aline', 'date':2, 'amount':3.78}
		,{'user_name':'aline', 'date':3, 'amount':2.20}
	]

