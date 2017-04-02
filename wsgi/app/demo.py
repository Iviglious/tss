""" This module handles the route calls to the demo page """

from datetime import datetime
from flask import request

from app import C_APP, DB, BoK


@C_APP.route('/demo/')
def demo():
    """ Routing function for demo (GET) """
	# read from db to get all expenses and visualise them
    all_expenses = DB.get_all_expenses()

	#html = render_template("demo.html", form=ExpenseForm(), expenses=all_expenses, message=None)
    return BoK.generate_bar_tab(None, all_expenses)

@C_APP.route('/demo/', methods=['POST'])
def demo_post():
    """ Routing function for demo POST. Adding a new expense. """

    user_name = request.form['user_name']
    expense_date = datetime.strptime(request.form['expense_date'], '%Y-%m-%d')
    expense_amount = float(request.form['expense_amount'])
    expense_description = request.form['expense_description']

    msg = None
    if user_name: # it's a request to add a new expense
        msg = DB.add_expense(user_name, expense_date, expense_amount, expense_description)

	# read from db to get all expenses and visualise them
    all_expenses = DB.get_all_expenses()

	#html = render_template("demo.html", form=ExpenseForm(), expenses=all_expenses, message=msg)
	#return html
    return BoK.generate_bar_tab(msg, all_expenses)
